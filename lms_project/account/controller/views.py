import bcrypt
import random
import string
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from rest_framework import viewsets, status
from rest_framework.response import Response
from account.serializers import ProfileSerializer
from account.service.account_service_impl import AccountServiceImpl

from google_oauth.service.redis_service_impl import RedisServiceImpl


class AccountView(viewsets.ViewSet):
    accountService = AccountServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def checkEmailDuplication(self, request):
        print("checkEmailDuplication()")
        try:
            email = request.data.get("email")
            isDuplicate = self.accountService.checkEmailDuplication(email)
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
                img="0",
                Attendance_cherry="0",
                Attendance_date="0",
            )

            serializer = ProfileSerializer(account)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
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
        try:
            email = request.data.get("email")
            isLoginType = self.accountService.checkLoginType(email)
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
            success = self.accountService.changePassword(email, hashed_password)
            return Response(
                {
                    "success": success
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print("changeNewPassword 중 에러 발생:", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def getProfileImg(self, request):
        try:
            email = request.data.get("email")
            getProfileImg = self.accountService.checkProfileImg(email)
            return Response(
                {
                    "getProfileImg": getProfileImg
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print("getProfileImg 중 에러 발생:", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def setProfileImg(self, request):
        try:
            email = request.data.get("email")
            img_id = request.data.get("img_id")
            setProfileImg = self.accountService.settingProfileImg(email, img_id)
            return Response(
                {
                    "setProfileImg": setProfileImg
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print("setProfileImg 중 에러 발생:", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def getAccountCreateTime(self, request):
        try:
            email = request.data.get("email")
            getCreateTime = self.accountService.checkAccountCreateTime(email)
            return Response(
                {
                    "getCreateTime": getCreateTime
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print("getCreateTime 중 에러 발생:", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def sendResetEmail(self, request):
        try:
            email = request.data.get("email")
            if not email:
                return Response({"error": "이메일 주소를 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)

            # 이메일 주소가 유효한지 확인
            account = self.accountService.findAccountByEmail(email)
            if not account:  # account가 False일 때
                return Response({"error": "등록되지 않은 이메일 주소입니다."}, status=status.HTTP_404_NOT_FOUND)

            # 5글자 재설정 코드 생성
            reset_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

            # 코드 만료 시간 설정 (예: 1시간 후)
            code_expiry = timezone.now() + timedelta(hours=1)

            # 계정에 코드와 만료 시간 저장
            account.reset_password_code = reset_code
            account.reset_password_code_expiry = code_expiry
            account.save()

            # 이메일 내용 작성
            email_subject = "비밀번호 재설정 요청"
            email_message = f"""
            안녕하세요,

            비밀번호 재설정 요청을 받았습니다. 아래의 코드를 입력하여 새 비밀번호를 설정해 주세요:

            재설정 코드: {reset_code}

            이 코드는 1시간 동안 유효합니다.

            만약 비밀번호 재설정을 요청하지 않으셨다면, 이 이메일을 무시해 주세요.

            감사합니다.
            """

            # 이메일 전송
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            return Response({"message": "비밀번호 재설정 이메일을 발송했습니다."}, status=status.HTTP_200_OK)

        except Exception as e:
            print("비밀번호 재설정 이메일 발송 중 오류 발생:", e)
            return Response({"error": "이메일 발송 중 오류가 발생했습니다."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
