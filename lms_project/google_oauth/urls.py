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
    path('redis-get-paid-member-type', GoogleOauthView.as_view({'post': 'getUserTokenPaidMemberTypeInfo'}),
         name='redis-get-paid-member-type'),
    path('redis-get-ticket', GoogleOauthView.as_view({'post': 'getUserTicketInfo'}), name='redis-get-ticket'),
    path('redis-get-nickname', GoogleOauthView.as_view({'post': 'getUserNicknameInfo'}), name='redis-get-nickname'),
    path('redis-update-ticket', GoogleOauthView.as_view({'post': 'updateUserTicket'}), name='redis-update-user-ticket'),
    path('redis-get-cherry', GoogleOauthView.as_view({'post': 'getUserCherryInfo'}), name='redis-get-cherry'),
    path('redis-purchase-ticket', GoogleOauthView.as_view({'post': 'purchaseTicket'}), name='redis-purchase-ticket'),
    path('redis-update-cherry', GoogleOauthView.as_view({'post': 'updateUserCherry'}), name='redis-update-user-cherry'),
    path('redis-purchase-cherry', GoogleOauthView.as_view({'post': 'purchaseCherry'}), name='redis-purchase-cherry'),
    path('logout', GoogleOauthView.as_view({'post': 'dropRedisTokenForLogout'}), name='drop-redis-token-for-logout'),
    path('readyKakaoPay',GoogleOauthView.as_view({'post': 'ReadyKakaoPay'}),name='readykakaoPay-test'),
    path('approveKakaoPay',GoogleOauthView.as_view({'post': 'ApproveKakaoPay'}),name='approvekakaoPay-test'),
    path('redis-add-attendancecherry',GoogleOauthView.as_view({'post': 'addAttendanceCherry'}),name='redis-add-attendancecherry'),
    path('redis-get-account-id', GoogleOauthView.as_view({'post': 'getAccountIdFromUserToken'}), name='redis-get-account-id'),
    path('save-recipe-to-redis', GoogleOauthView.as_view({'post': 'saveRecipeToRedis'}), name='save-recipe-to-redis'),
]
