import bcrypt

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

    def getAttendanceDateList(self, request):
        try:
            print(request.data)
            user_token = request.data.get('usertoken')
            print("user_token 가져오기:", user_token)
            accountInfo = self.redisService.getValueByKey(user_token)
            print('현재 accountInfo:', accountInfo)
            account_id = accountInfo['account_id']
            print('이 유저의 유저 id 반환:', account_id)

            attendanceDateList = self.accountService.findAttendance_DateByAccountId(account_id)
            print('반환 예정인 부분:', {'attendanceDateList': attendanceDateList})
            return Response({'attendanceDateList': attendanceDateList}, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error get user's Attendance Date List:{e}")
            return False, str(e)
