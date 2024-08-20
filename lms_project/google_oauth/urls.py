from django.urls import path, include
from rest_framework.routers import DefaultRouter
from google_oauth.controller.views import GoogleOauthView

router = DefaultRouter()
router.register(r'', GoogleOauthView, basename='google_oauth')

urlpatterns = [
    path('', include(router.urls)),
    path('login', GoogleOauthView.as_view({'post': 'GoogleLoginToken'}), name='google-login'),
    path('redis-access-token', GoogleOauthView.as_view({'post': 'redisAccessToken'}), name='redis-access-token'),
    path('redis-get-email', GoogleOauthView.as_view({'post': 'getUserTokenEmailInfo'}), name='redis-get-value'),
    path('redis-get-paid-member-type', GoogleOauthView.as_view({'post': 'getUserTokenPaidMemberTypeInfo'}), name='redis-get-paid-member-type'),
    path('redis-get-ticket', GoogleOauthView.as_view({'post': 'getUserTicketInfo'}), name='redis-get-ticket'),
    path('redis-get-nickname', GoogleOauthView.as_view({'post': 'getUserNicknameInfo'}), name='redis-get-nickname'),
    path('redis-update-ticket', GoogleOauthView.as_view({'post': 'updateUserTicket'}), name='redis-update-user-ticket'),
]
