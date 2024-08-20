from datetime import datetime, timedelta

import bcrypt
import jwt

from account.entity.account_login_type import AccountLoginType
from account.entity.profile import Profile
from account.repository.profile_repository import ProfileRepository
from lms_project import settings


class ProfileRepositoryImpl(ProfileRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def findByEmail(self, email):
        try:
            profile = Profile.objects.get(email=email)
            return profile
        except Profile.DoesNotExist:
            print(f"email 찾을 수 없음: {email}")
            return None
        except Exception as e:
            print(f"email 검사 중 에러: {e}")
            return None

    def create(self, email, password, nickname, account):
        profile = Profile.objects.create(
            email=email,
            password=password,
            nickname=nickname,
            account=account,
        )
        return profile

    def createSocial(self, email, account):
        profile = Profile.objects.create(
            email=email,
            password="N/A",
            account=account,
        )
        return profile

    def decryption(self, email, password):
        try:
            account = Profile.objects.filter(email=email).first()

            if account is None:
                return None

            if bcrypt.checkpw(password.encode("utf-8"), account.password.encode("utf-8")):
                payload = {
                    'id': account.id,
                    'email': email,
                    'exp': datetime.utcnow() + timedelta(hours=24)
                }
                access_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
                return access_token
            else:
                return None

        except Exception as e:
            print(f"decryption 중 에러 발생: {e}")
            return None

    def findByLoginType(self, email):
        try:
            profile = Profile.objects.get(email=email)
            login_type = AccountLoginType.objects.get(id=profile.id)
            print("로그인의 로그인 타입",login_type.loginType)
            return login_type.loginType
        except Profile.DoesNotExist:
            print(f"email 찾을 수 없음: {email}")
            return None
        except Exception as e:
            print(f"email 검사 중 에러: {e}")
            return None
        pass

    def findByAccount(self, accountId):
        try:
            profile = Profile.objects.get(id=accountId)
            email = Profile.objects.get(email=profile.id)
            return email
        except Profile.DoesNotExist:
            print(f"accountId 찾을 수 없음: {email}")
            return None
        except Exception as e:
            print(f"accountId 검사 중 에러: {e}")
            return None

    def findByNickname(self, nickname):
        try:
            profile = Profile.objects.get(nickname=nickname)
            return profile
        except Profile.DoesNotExist:
            print(f"email 찾을 수 없음: {nickname}")
            return None
        except Exception as e:
            print(f"email 검사 중 에러: {e}")
            return None