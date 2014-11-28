import time
import sys
import datetime
import math

class TwitterRequest(object):
    def __init__(self):
        #twitter documentation
        #https://dev.twitter.com/rest/reference/get/search/tweets
        self._request= None

    #SEARCH_PARAM
    @property
    def request(self):
        return self._request

    @request.setter
    def search_param(self,value):
        self._request = value

    @request.deleter
    def search_param(self):
        del self._request


    def make_request(self):
        #read in all the parameters for the API call
        try:
            if self._request._keyword is None:
                raise Exception("'q' Parameter cannot be None!")
            else:
                q = self._request._keyword
        except:
            raise Exception("'q' Parameter not defined!")
        try:
            geocode = self._request._geocode
        except:
            raise Exception("'geocode' Parameter not defined!")
        try:
            lang = self._request._lang
        except:
            raise Exception("'lang' Parameter not defined!")
        try:
            result_type = self._request._result_type
        except:
            raise Exception("'result_type' Parameter not defined!")
        try:
            if self._request._max_results is None:
                #twitter default is 15
                count = 15
            elif self._request._max_results <= 100:
                count = self._request._max_results
            else:
                count = self._request._max_results
                print("WARNING: will induce multiple requests!")
        except:
            raise Exception("'count' Parameter not defined!")
        try:
            until = self._request._max_date
        except:
            raise Exception("'until' Parameter not defined!")

        #for paging read tweets older than max_id
        max_id = None
        data = {}
        if count > 100:
            while count > 100:
                start_time = datetime.datetime.now()
                request = self._request._search_auth.search(q=q, geocode=geocode, lang=lang,
                                    result_type=result_type, count=100, until=until, max_id=max_id)

                #add request results to output
                if max_id is None:
                    data = request["statuses"]
                else:
                    data.extend(request["statuses"])

                #read the results to get the last id and pass as max_id
                count_returned = request["search_metadata"]["count"]
                max_id = request["search_metadata"]["max_id"]

                #if no more tweets break out of loop
                if count_returned == 0:
                    count_returned = sys.maxint
                count -= count_returned

                #Rate Handling
                #twitter rate limits at 180/15min = 1/5sec
                end_time = datetime.datetime.now()
                elapsed_sec = (end_time - start_time).total_seconds()
                time.sleep(5 - elapsed_sec)

        #make final request
        request = self._request._search_auth.search(q=q, geocode=geocode, lang=lang,
                                result_type=result_type, count=count, until=until, max_id=max_id)
        #add request results to output
        if max_id is None:
            data = request["statuses"]
        else:
            data.extend(request["statuses"])
        return data

    def estimate_time(self):
        #see twitter rate handling for more info
        #last update 2014-11-28
        max_call_results = 100
        num_requests = math.ceil(self._request._max_results / max_call_results)
        api_rate = 5
        estimate_completion = num_requests * api_rate
        return estimate_completion