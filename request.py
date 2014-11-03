import twython
import search
import time
import sys

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
    def session_auth(self,value):
        self._session_auth = value

    @session_auth.deleter
    def session_auth(self):
        del self._session_auth


    def make_request(self):
        #read in all the parameters for the API call
        api_url = 'https://api.twitter.com/1.1/search/tweets.json'
        #
        try:
            if self._req_param._keyword is None:
                raise Exception("Keyword Parameter cannot be None!")
            else:
                q = self._req_param._keyword
        except:
            raise Exception("Keyword Parameter not defined!")
        try:
            geocode = self._req_param._geocode
        except:
            geocode = None
        try:
            lang = self._req_param._lang
        except:
            lang = None
        try:
            result_type = self._req_param._result_type
        except:
            result_type = None
        try:
            count = self._req_param._max_results
        except:
            count = None
        try:
            until = self._req_param._max_date
        except:
            until = None

        #for paging read tweets older than max_id
        max_id = None
        if count > 100:
            while count > 100:
                start_time = time()
                request = self._session_auth.search(api_url, q=q, geocode=geocode, lang=lang,
                                    result_type=result_type, count=100, until=until, max_id=max_id)

                #read the results to get the last id and pass as max_id
                count_returned = request["search_metadata"]["count"]
                max_id = request["search_metadata"]["max_id"]

                #if no more tweets break out of loop
                if count_returned == 0:
                    count_returned = sys.maxint
                count -= count_returned
                elapsed_time = time() - start_time

                #Rate Handling
                #twitter rate limits at 180/15min = 1/5sec
                time.sleep(5 - elapsed_time)
        else:
            #make request
            request = self._session_auth.search(api_url, q=q, geocode=geocode, lang=lang,
                                result_type=result_type, until=until)
            return request