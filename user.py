import Twython

class TwitterUser:
    def session_auth(app_key, app_secret, oauth_token, oauth_token_secret):
        return Twython(app_key, app_secret, oauth_token, oauth_token_secret)
        #test credentials
        #APP_KEY = '37ZrxAQkWjZi5Mj7euFk0fT2e'
        #APP_SECRET = 'Bo5duJpMC3iLHeZuOKyIkZJsOoLcnXbnCfURsrawCZPIp908t3'
        #OAUTH_TOKEN = '39855951-6MtVemzUgai6hQRMOhNVldha8Fa8nAQoNmfmZYqII'
        #OAUTH_TOKEN_SECRET = '6I3GlIJ1o4T0DB634KcQRQYghreLkv3jGmeZLIV3Amw68'
