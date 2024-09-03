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
            self.redis_client.hset(userToken, 'attendance_date1', attendance_date[0])
            self.redis_client.hset(userToken, 'attendance_date2', attendance_date[1])
            self.redis_client.hset(userToken, 'attendance_date3', attendance_date[2])
            self.redis_client.hset(userToken, 'attendance_date4', attendance_date[3])
            self.redis_client.hset(userToken, 'attendance_date5', attendance_date[4])
            self.redis_client.hset(userToken, 'attendance_date6', attendance_date[5])
            self.redis_client.hset(userToken, 'attendance_date7', attendance_date[6])
            self.redis_client.hset(userToken, 'attendance_date8', attendance_date[7])
            self.redis_client.hset(userToken, 'attendance_date9', attendance_date[8])
            self.redis_client.hset(userToken, 'attendance_date10', attendance_date[9])
            self.redis_client.hset(userToken, 'attendance_date11', attendance_date[10])
            self.redis_client.hset(userToken, 'attendance_date12', attendance_date[11])
            self.redis_client.hset(userToken, 'attendance_date13', attendance_date[12])
            self.redis_client.hset(userToken, 'attendance_date14', attendance_date[13])
            self.redis_client.hset(userToken, 'attendance_date15', attendance_date[14])
            self.redis_client.hset(userToken, 'attendance_date16', attendance_date[15])
            self.redis_client.hset(userToken, 'attendance_date17', attendance_date[16])
            self.redis_client.hset(userToken, 'attendance_date18', attendance_date[17])
            self.redis_client.hset(userToken, 'attendance_date19', attendance_date[18])
            self.redis_client.hset(userToken, 'attendance_date20', attendance_date[19])
            self.redis_client.hset(userToken, 'attendance_date21', attendance_date[20])
            self.redis_client.hset(userToken, 'attendance_date22', attendance_date[21])
            self.redis_client.hset(userToken, 'attendance_date23', attendance_date[22])
            self.redis_client.hset(userToken, 'attendance_date24', attendance_date[23])
            self.redis_client.hset(userToken, 'attendance_date25', attendance_date[24])
            self.redis_client.hset(userToken, 'attendance_date26', attendance_date[25])
            self.redis_client.hset(userToken, 'attendance_date27', attendance_date[26])
            self.redis_client.hset(userToken, 'attendance_date28', attendance_date[27])
            self.redis_client.hset(userToken, 'attendance_date29', attendance_date[28])
            self.redis_client.hset(userToken, 'attendance_date30', attendance_date[29])
            self.redis_client.hset(userToken, 'attendance_date31', attendance_date[30])
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
