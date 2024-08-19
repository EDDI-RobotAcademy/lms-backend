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
    path('redis-get-paidmembertype', GoogleOauthView.as_view({'post': 'getUserTokenPaidMemberTypeInfo'}), name='redis-get-paidmembertype'),
]
