from rest_framework import viewsets, status
from rest_framework.response import Response

from google_oauth.service.google_oauth_service_impl import GoogleOauthServiceImpl
from lms_project import settings
from google.oauth2 import id_token
from google.auth.transport import requests

class GoogleOauthView(viewsets.ViewSet):
    googleOauthService = GoogleOauthServiceImpl.getInstance()

    def GoogleLoginToken(self, request):
        token = request.data.get('credential')
        clientId = request.data.get('clientId')
        try:
            tokenInfo = id_token.verify_oauth2_token(token, requests.Request(), clientId)

            userInfo = self.googleOauthService.googleTokenDecoding(tokenInfo)

            return Response({
                'email': userInfo['email'],
                'name': userInfo['name'],
            }, status=200)
        except Exception as e:
            print("토큰 인코딩 오류 발생:", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)