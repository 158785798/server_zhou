from fastapi import APIRouter
from . import views

blogs_router = APIRouter()


blogs_router.add_api_route('/like', views.like, methods=['get'])
blogs_router.add_api_route('/dislike', views.dislike, methods=['get'])
blogs_router.add_api_route('/get_taste', views.get_taste, methods=['get'])
blogs_router.add_api_route('/get_emojis', views.get_emojis, methods=['get'])
blogs_router.add_api_route('/get_comments', views.get_comments, methods=['get'])
blogs_router.add_api_route('/get_blogs', views.get_blogs, methods=['get'])
blogs_router.add_api_route('/get_blog', views.get_blog, methods=['get'])
blogs_router.add_api_route('/get_box_msg', views.get_box_msg, methods=['get'])
blogs_router.add_api_route('/get_msg_count', views.get_msg_count, methods=['get'])
blogs_router.add_api_route('/click_msg', views.click_msg, methods=['get'])


blogs_router.add_api_route('/comment', views.comment, methods=['post'])
blogs_router.add_api_route('/publish_blog', views.publish_blog, methods=['post'])


blogs_router.add_api_route('/del_blog', views.del_blog, methods=['delete'])
blogs_router.add_api_route('/del_comment', views.del_comment, methods=['delete'])

