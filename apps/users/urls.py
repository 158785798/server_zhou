from fastapi import APIRouter
from . import views

users_router = APIRouter()

users_router.add_api_route('/check_user', views.check_user, methods=['get'])
users_router.add_api_route('/get_images', views.get_images, methods=['get'])
users_router.add_api_route('/get_album', views.get_album, methods=['get'])
users_router.add_api_route('/follow_in', views.follow_in, methods=['get'])
users_router.add_api_route('/follow_out', views.follow_out, methods=['get'])
users_router.add_api_route('/get_fans', views.get_fans, methods=['get'])
users_router.add_api_route('/save_bio', views.save_bio, methods=['get'])
users_router.add_api_route('/get_userinfo', views.get_userinfo, methods=['get'])
users_router.add_api_route('/get_email_code', views.get_email_code, methods=['get'])

users_router.add_api_route('/login', views.login, methods=['post'])
users_router.add_api_route('/signUp', views.get_email_code, methods=['post'])
users_router.add_api_route('/upload_b64', views.upload_b64, methods=['post'])
users_router.add_api_route('/upload_binary', views.upload_binary, methods=['post'])
users_router.add_api_route('/password_reset', views.password_reset, methods=['post'])
