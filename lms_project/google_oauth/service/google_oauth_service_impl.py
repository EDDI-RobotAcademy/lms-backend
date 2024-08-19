from google_oauth.service.google_oauth_service import GoogleOauthService


class GoogleOauthServiceImpl(GoogleOauthService):
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

    def googleTokenDecoding(self, tokenInfo):
        try:
            if tokenInfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')

            user_info = {
                'sub': tokenInfo['sub'],
                'email': tokenInfo['email'],
                'name': tokenInfo.get('name', 'No name provided')
            }

            return user_info

        except ValueError as e:
            raise ValueError(f"Token verification failed: {str(e)}")

