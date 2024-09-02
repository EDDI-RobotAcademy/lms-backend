import redis
from django.conf import settings

from google_oauth.service.redis_service import RedisService


class RedisServiceImpl(RedisService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.redis_client = redis.StrictRedis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                password=settings.REDIS_PASSWORD,
                decode_responses=True
            )

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def store_access_token(self, userToken, account_id, nickname, email, ticket, cherry, attendance_cherry,
                           attendance_date):
        try:
            self.redis_client.hset(userToken, 'account_id', str(account_id))
            self.redis_client.hset(userToken, 'nickname', nickname)
            self.redis_client.hset(userToken, 'email', email)
            self.redis_client.hset(userToken, 'ticket', ticket)
            self.redis_client.hset(userToken, 'cherry', cherry)
            self.redis_client.hset(userToken, 'attendance_cherry', attendance_cherry)
            self.redis_client.hset(userToken, 'attendance_date', attendance_date)
            self.redis_client.hset(userToken, 'attendance_date', attendance_date)
            self.redis_client.hset(userToken, 'attendance_date', attendance_date)
            self.redis_client.hset(userToken, 'attendance_date', attendance_date)
            self.redis_client.hset(userToken, 'attendance_date', attendance_date)
            self.redis_client.hset(userToken, 'attendance_date', attendance_date)
        except Exception as e:
            print('Error storing access token in Redis:', e)
            raise e

    def getValueByKey(self, key):
        try:
            data = self.redis_client.hgetall(key)
            if not data:
                print(f"No data found for key: {key}")
                return None
            return {k.decode('utf-8') if isinstance(k, bytes) else k:
                        v.decode('utf-8') if isinstance(v, bytes) else v
                    for k, v in data.items()}
        except Exception as e:
            print(f'Error retrieving data from Redis: {e}')
            return None

    def deleteKey(self, key):
        try:
            result = self.redis_client.delete(key)
            if result == 1:
                print(f"유저 토큰 삭제 성공: {key}")
                return True

            return False
        except Exception as e:
            print("redis key 삭제 중 에러 발생:", e)
            raise e

    def update_access_token(self, userToken, accountInfo):
        try:
            ticket = accountInfo['ticket']
            self.redis_client.hset(userToken, 'ticket', ticket)
            return True
        except Exception as e:
            print(f"Error updating access token in Redis: {e}")
            return False

    def update_cherry_count(self, userToken, accountInfo):
        try:
            cherry = accountInfo['cherry']
            self.redis_client.hset(userToken, 'cherry', cherry)
            return True
        except Exception as e:
            print(f"Error updating access token in Redis: {e}")
            return False

    def update_attendance_cherry_count(self, user_token, accountInfo):
        try:
            attendance_cherry = accountInfo['attendance_cherry']
            self.redis_client.hset(user_token, 'attendance_cherry', attendance_cherry)
            return True

        except Exception as e:
            print(f"Error updating attendance cherry in redis: {e}")
            return False

    def get_account_id_by_usertoken(self, userToken):
        try:
            account_info = self.getValueByKey(userToken)
            if not account_info:
                print(f"User token not found: {userToken}")
                return None

            account_id = account_info.get('account_id')
            return account_id if account_id else False

        except Exception as e:
            print(f"Error retrieving account_id from Redis: {e}")
            return False
