from datetime import datetime, timedelta

import bcrypt
import jwt

from rest_framework import viewsets, status
from rest_framework.response import Response

from account.entity.profile import Profile
from account.serializers import ProfileSerializer
from account.service.account_service_impl import AccountServiceImpl

from django.conf import settings


class AccountView(viewsets.ViewSet):
    accountService = AccountServiceImpl.getInstance()

    def checkEmailDuplication(self, request):
        print("checkEmailDuplication()")
        try:
            email = request.data.get("email")
            isDuplicate = self.accountService.checkEmailDuplication(email)
            print("Email 이미 존재" if isDuplicate else "Email 사용 가능")
            return Response(
                {
                    "isDuplicate": isDuplicate
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print("이메일 중복 체크 중 에러 발생:", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def registerAccount(self, request):
        try:
            email = request.data.get("email")
            password = request.data.get("password")
            nickname = request.data.get("nickname")

            hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

            account = self.accountService.registerAccount(
                loginType="NORMAL",
                paidmemberType="0",
                Ticket="99999",
                Cherry="99999",
                email=email,
                password=hashed_password,
                nickname=nickname,
                Attendance_cherry="0",
                Attendance_date="0",
            )

            serializer = ProfileSerializer(account)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print("계정 생성 중 에러 발생1:", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def registerSocialAccount(self, request):
        try:
            email = request.data.get("email")

            account = self.accountService.registerSocialAccount(
                loginType="GOOGLE",
                paidmemberType=0,
                email=email,
            )

            serializer = ProfileSerializer(account)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print("계정 생성 중 에러 발생:", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def loginAccount(self, request):
        try:
            print("settings.SECRET_KEY", settings.SECRET_KEY)
            email = request.data.get("email")
            password = request.data.get("password")

            access_token = self.accountService.decryptionPassword(email, password)

            return Response({
                "access_token": access_token,
                "token_type": "Bearer"
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print("로그인 중 에러 발생:", e)
            return Response({"error": "로그인 중 오류 발생"}, status=status.HTTP_400_BAD_REQUEST)

    def checkLoginType(self, request):
        print("checkLoginType()")
        try:
            email = request.data.get("email")
            isLoginType = self.accountService.checkLoginType(email)
            print("isLoginType", isLoginType)
            return Response(
                {
                    "isLoginType": isLoginType
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print("이메일 중복 체크 중 에러 발생:", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def checkNickNameDuplication(self, request):
        print("checkNickNameDuplication()")
        try:
            nickname = request.data.get("nickname")
            isNickNameDuplicate = self.accountService.checkNickNameDuplication(nickname)
            print("Nickname 이미 존재" if isNickNameDuplicate else "nickname 사용 가능")
            return Response(
                {
                    "isNickNameDuplicate": isNickNameDuplicate
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print("이메일 중복 체크 중 에러 발생:", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def changeNewPassword(self, request):
        print("changeNewPassword()")
        try:
            newpassword = request.data.get("password")
            email = request.data.get("email")
            hashed_password = bcrypt.hashpw(newpassword.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
            print(" 새로운 비밀번호 ", hashed_password)
            success = self.accountService.changePassword(email, hashed_password)
            print("True" if success else "False")
            return Response(
                {
                    "success": success
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print("changeNewPassword 중 에러 발생:", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
