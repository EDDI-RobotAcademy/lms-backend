import bcrypt

from rest_framework import viewsets, status
from rest_framework.response import Response

from account.serializers import ProfileSerializer
from account.service.account_service_impl import AccountServiceImpl

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

            hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

            account = self.accountService.registerAccount(
                email=email,
                password=hashed_password,
            )

            serializer = ProfileSerializer(account)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print("계정 생성 중 에러 발생:", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

