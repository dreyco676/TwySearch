import time
import sys

class TwitterRequest(object):
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
        try:
            if self._req_param._keyword is None:
                raise Exception("'q' Parameter cannot be None!")
            else:
                q = self._req_param._keyword
        except:
            raise Exception("'q' Parameter not defined!")
        try:
            geocode = self._req_param._geocode
        except:
            raise Exception("'geocode' Parameter not defined!")
        try:
            lang = self._req_param._lang
        except:
            raise Exception("'lang' Parameter not defined!")
        try:
            result_type = self._req_param._result_type
        except:
            raise Exception("'result_type' Parameter not defined!")
        try:
            if self._req_param._max_results is None:
                #twitter default is 15
                count = 15
            elif self._req_param._max_results > 100:
                count = self._req_param._max_results
                print("WARNING: will induce multiple requests!")
        except:
            raise Exception("'count' Parameter not defined!")
        try:
            until = self._req_param._max_date
        except:
            raise Exception("'until' Parameter not defined!")

        #for paging read tweets older than max_id
        max_id = None
        if count > 100:
            data = {}
            while count > 100:
                start_time = time()
                request = self._session_auth.search(q=q, geocode=geocode, lang=lang,
                                    result_type=result_type, count=100, until=until, max_id=max_id)

                #read the results to get the last id and pass as max_id
                count_returned = request["search_metadata"]["count"]
                max_id = request["search_metadata"]["max_id"]

                #if no more tweets break out of loop
                if count_returned == 0:
                    count_returned = sys.maxint
                count -= count_returned
                elapsed_time = time() - start_time

                #add request results to output
                data.update(request["statuses"])
                #Rate Handling
                #twitter rate limits at 180/15min = 1/5sec
                time.sleep(5 - elapsed_time)
        else:
            #make request
            request = self._session_auth.search(q=q, geocode=geocode, lang=lang,
                                result_type=result_type, count=count, until=until)
            data = request["statuses"]
            return data

    def estimate_time(self):
        print("time estimate placeholder")