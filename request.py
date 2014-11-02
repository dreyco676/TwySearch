import twython

class TwitterRequest:
    def __init__(self):
        #twitter documentation
        #https://dev.twitter.com/rest/reference/get/search/tweets
        self._req_param = None
        self._session_auth = None

    #SEARCH_PARAM
    @property
    def req_param(self):
        return self._req_param

    @req_param.setter
    def search_param(self,value):
        self._req_param = value

    @req_param.deleter
    def search_param(self):
        del self._req_param

    #SESSION_AUTH
    @property
    def session_auth(self):
        return self._session_auth

    @session_auth.setter
    def search_param(self,value):
        self._session_auth = value

    @session_auth.deleter
    def search_param(self):
        del self._session_auth


    def make_request(self):
        if self.search_params._max_results > 100:
            while self.search_params.max_results > 100:
                twython.search(self.search_params)
        else:
            #make request
            twython.search(self.search_params)
