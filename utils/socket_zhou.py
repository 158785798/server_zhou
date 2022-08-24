import json
import sys
from copy import copy

import socketio
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import JSONResponse
from starlette.routing import Mount

from apps.users.urls import users_router
from apps.blogs.urls import blogs_router
from utils.middlewares import BasicAuthBackend


def on_auth_error(request, exc):
    return JSONResponse({'code': 401, 'msg': '请重新登录！'})


if sys.platform == 'win32':
    routes = [Mount('/api/static', StaticFiles(directory='static'), name='static')]
else:
    routes = None

fast_app = FastAPI(routes=routes)

router = APIRouter(prefix='/api')
router.include_router(users_router)
router.include_router(blogs_router)
fast_app.include_router(router)

fast_app.add_middleware(AuthenticationMiddleware, backend=BasicAuthBackend(), on_error=on_auth_error)
fast_app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False,
                        allow_methods=["*"], allow_headers=["*"])

mgr = socketio.AsyncRedisManager()  # 使用redis作为消息队列

sio = socketio.AsyncServer(  # 使用socketio
    async_mode='asgi',
    cors_allowed_origins='*',
    client_manager=mgr,
    # namespaces='*'
)


class SocketManager:
    def __init__(self):
        self.conns = {}
        self.fast_app = fast_app
        self.sio = sio
        self.sio.on('connect', self.connect)
        self.sio.on('disconnect', handler=self.disconnect)
        self.sio.on('chat', handler=self.chat)
        self.sio.on('broadcast', handler=self.broadcast)

    async def connect(self, sid, *args):
        username = args[0]['QUERY_STRING'].split('&')[0].split('=')[-1]
        if username not in self.conns:
            self.conns[username] = sid
        await self.sio.emit('online', username)

    async def chat(self, sid, data):
        tmp_dict = json.loads(data)
        username = tmp_dict['username']
        await self.send('chat', data=data, username=username)

    async def broadcast(self, sid, data):
        tmp_dict = json.loads(data)
        username = tmp_dict['username']
        skip_sid = self.conns.get(username)
        await self.sio.emit('broadcast', data=data, skip_sid=skip_sid)

    async def disconnect(self, sid):
        tmp_conns = copy(self.conns)
        for k, v in tmp_conns.items():
            if sid == v:
                self.conns.pop(k, None)

    async def send(self, ev, data=None, username=None):
        room = self.conns.get(username)
        if room is not None:
            await self.sio.emit(ev, data=data, room=room)
