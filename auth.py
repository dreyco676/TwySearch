from twython import Twython
import json

class TwitterUser:
    def __init__(self):
        self._app_key = None
        self._app_secret = None
        self._oauth_token = None
        self._oauth_token_secret = None

    #APP_KEY
    @property
    def app_key(self):
        return self._app_key

    @app_key.setter
    def app_key(self, value):
        self._app_key = value

    @app_key.deleter
    def app_key(self):
        del self._app_key

    #APP_SECRET
    @property
    def app_secret(self):
        return self._app_secret

    @app_secret.setter
    def app_secret(self, value):
        self._app_secret = value

    @app_secret.deleter
    def app_secret(self):
        del self._app_secret

    #OAUTH_TOKEN
    @property
    def oauth_token(self):
        return self._oauth_token

    @oauth_token.setter
    def oauth_token(self, value):
        self._oauth_token = value

    @oauth_token.deleter
    def oauth_token(self):
        del self._oauth_token

    #OAUTH_TOKEN_SECRET
    @property
    def oauth_token_secret(self):
        return self._oauth_token_secret

    @oauth_token_secret.setter
    def oauth_token_secret(self, value):
        self._oauth_token_secret = value

    @oauth_token_secret.deleter
    def oauth_token_secret(self):
        del self._oauth_token_secret

    def read_json(self):
        json_data = open('auth.json')
        data = json.load(json_data)
        try:
            self._app_key = data["app_key"]
        except:
            print("Error reading app_key")
        try:
            self._app_secret = data["app_secret"]
        except:
            print("Error reading app_secret")
        try:
            self._oauth_token = data["oauth_token"]
        except:
            print("Error reading oauth_token")
        try:
            self._oauth_token_secret = data["oauth_token_secret"]
        except:
            print("Error reading oauth_token_secret")
        json_data.close()

    def auth(self):
        twitter_auth = Twython(self._app_key, self._app_secret, self._oauth_token, self._oauth_token_secret)
        return twitter_auth

