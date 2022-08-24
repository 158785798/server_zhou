from starlette.authentication import AuthenticationBackend, AuthCredentials, AuthenticationError

import settings
from utils.jwt_auth import verify_token


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        if not request.scope['scheme'].startswith('ws'):
            path = request.url.path.split('/')[-1]
            if path not in settings.WHITE_LIST and 'static' not in request.url.path:
                token = request.headers.get("Authorization", '')
                user = await verify_token(token)

                if user is None:
                    raise AuthenticationError('Invalid basic auth credentials')
                else:
                    return AuthCredentials(["authenticated"]), user
