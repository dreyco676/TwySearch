import request

class TwitterSearch(object):
    def __init__(self):
        self._keyword = None
        self._geocode = None
        self._lang = None
        self._result_type = None
        self._max_results = None
        self._max_date = None
        #twitter documentation
        #https://dev.twitter.com/rest/reference/get/search/tweets

    #KEYWORD
    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self,value):
        self._keyword = value

    @keyword.deleter
    def keyword(self):
        del self._keyword

    #GEOCODE
    @property
    def geocode(self):
        return self._geocode

    @geocode.setter
    def geocode(self,value):
        self._geocode = value

    @geocode.deleter
    def geocode(self):
        del self._geocode

    #LANG
    @property
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self,value):
        self._lang = value

    @lang.deleter
    def lang(self):
        del self._lang

    #RESULT_TYPE
    @property
    def result_type(self):
        return self._result_type

    @result_type.setter
    def result_type(self,value):
        self._result_type = value

    @result_type.deleter
    def result_type(self):
        del self._result_type

    #MAX_RESULTS
    @property
    def max_results(self):
        return self._max_results

    @max_results.setter
    def max_results(self,value):
        self._max_results = value

    @max_results.deleter
    def max_results(self):
        del self._max_results

    #MAX_DATE
    @property
    def max_date(self):
        return self._max_date

    @max_date.setter
    def max_date(self,value):
        self._max_date = value

    @max_date.deleter
    def max_date(self):
        del self._max_date
