from account.entity.profile import Profile
from account.repository.profile_repository import ProfileRepository

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

    def create(self, email, password):
        profile = Profile.objects.create(
            email=email,
            password=password,
        )
        return profile