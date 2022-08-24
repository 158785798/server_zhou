import socketio

from utils.socket_zhou import SocketManager

sm = SocketManager()

app = socketio.ASGIApp(  # 整合socketio和fastapi
    socketio_server=sm.sio,
    other_asgi_app=sm.fast_app,
    socketio_path='/socket.io'
)
