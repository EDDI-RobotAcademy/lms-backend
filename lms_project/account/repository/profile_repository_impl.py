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

    def create(self, email, password, nickname, img, account):
        profile = Profile.objects.create(
            email=email,
            password=password,
            nickname=nickname,
            img=img,
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

            accountpassword = account.password.encode("utf-8")
            passwordencode = password.encode("utf-8")

            print("accountpassword", accountpassword)
            print("passwordencode", passwordencode)

            checkbcrypt = bcrypt.checkpw(password.encode("utf-8"), account.password.encode("utf-8"))
            print("checkbcrypt 체크", checkbcrypt)
            if checkbcrypt == True:
                payload = {
                    'id': account.id,
                    'email': email,
                    'exp': datetime.utcnow() + timedelta(hours=24)
                }
                access_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
                print("access_token 출력", access_token)
                return access_token
            else:
                print("checkbcrypt가 false임")
                return None

        except Exception as e:
            print(f"decryption 중 에러 발생: {e}")
            return None

    def findByLoginType(self, email):
        try:
            profile = Profile.objects.get(email=email)
            login_type = AccountLoginType.objects.get(id=profile.id)
            print("로그인의 로그인 타입", login_type.loginType)
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

    def findByNickname(self, accountId):
        try:
            account = Profile.objects.get(id=accountId)
            nickname = Profile.objects.get(nickname=account.nickname)
            return nickname.nickname
        except Exception as e:
            print(f"email 검사 중 에러: {e}")
            return None

    def updatePassword(self, email, newpassword):
        try:
            profile = Profile.objects.get(email=email)
            profile.password = newpassword
            profile.save()
            print("새 비밀번호가 성공적으로 저장되었습니다.")
            return True

        except Profile.DoesNotExist:
            print(f"해당 이메일({email})을 가진 사용자를 찾을 수 없습니다.")
            return False

        except Exception as e:
            print(f"updatePassword 중 에러 발생: {e}")
            return False

    def findByProfileImg(self, email):
        try:
            profile = Profile.objects.get(email=email)
            print("findByProfileImg의 profile", profile.img)
            return profile.img
        except Exception as e:
            print(f"findByProfileImg 중 에러: {e}")
            return None
        pass

    def updateProfileImg(self, email, img_id):
        try:
            profile = Profile.objects.get(email=email)
            profile.img = img_id
            profile.save()
            print("새 프로필이 성공적으로 저장되었습니다.")
            return img_id

        except Profile.DoesNotExist:
            print(f"해당 이메일({email})을 가진 사용자를 찾을 수 없습니다.")
            return False

        except Exception as e:
            print(f"updateProfileImg 중 에러 발생: {e}")
            return False
