from abc import ABC, abstractmethod


class RedisService(ABC):
    @abstractmethod
    def store_access_token(self, access_token, account_id, nickname, email, ticket, cherry):
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
