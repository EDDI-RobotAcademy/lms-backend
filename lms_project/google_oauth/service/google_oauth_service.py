from abc import ABC, abstractmethod

class GoogleOauthService(ABC):

    @abstractmethod
    def googleTokenDecoding(self, tokenInfo):
        pass