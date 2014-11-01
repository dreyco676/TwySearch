import user


class TwitterSearch:
    def __init__(self, keywords, params, session_auth):
        self.keywords = keywords
        self.params = params
        self.session_auth = user.TwitterUser
