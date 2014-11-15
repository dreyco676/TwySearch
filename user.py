import Twython

class TwitterUser:
    def __init__(self, name, company, app_key, app_secret, oauth_token, oauth_token_secret):
        self.name = name
        self.company = company
        self.app_key = app_key
        self.app_secret = app_secret
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret

    def get_auth(self):
        return Twython(self.app_key, self.app_secret, self.oauth_token, self.oauth_token_secret)

        #test credentials
        #APP_KEY = '37ZrxAQkWjZi5Mj7euFk0fT2e'
        #APP_SECRET = 'Bo5duJpMC3iLHeZuOKyIkZJsOoLcnXbnCfURsrawCZPIp908t3'
        #OAUTH_TOKEN = '39855951-6MtVemzUgai6hQRMOhNVldha8Fa8nAQoNmfmZYqII'
        #OAUTH_TOKEN_SECRET = '6I3GlIJ1o4T0DB634KcQRQYghreLkv3jGmeZLIV3Amw68'
