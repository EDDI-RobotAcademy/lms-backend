from abc import ABC, abstractmethod


class RedisService(ABC):
    @abstractmethod
    def store_access_token(self, userToken, account_id, nickname, email, ticket, cherry, attendance_cherry,
                           attendance_date):
        pass

    @abstractmethod
    def getValueByKey(self, key):
        pass

    @abstractmethod
    def deleteKey(self, key):
        pass

    @abstractmethod
    def update_access_token(self, userToken, accountInfo):
        pass

    @abstractmethod
    def update_attendance_cherry_count(self, user_token, accountInfo):
        pass

    @abstractmethod
    def update_attendance_status(self, user_token, account_attendance_status, today):
        pass

    @abstractmethod
    def get_account_id_by_usertoken(self, userToken):
        pass
