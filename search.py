import twython

class TwitterSearch:
    def __init__(self):
        self._keyword = None
        self._geocode = None
        self._lang = None
        self._max_results = None
        self._max_date = None
        #twitter documentation
        #https://dev.twitter.com/rest/reference/get/search/tweets

    #KEYWORD
    @property
    def keyword(self):
        print("Keyword property for search")
        return self._keyword

    @keyword.setter
    def keyword(self,value):
        print("Setter of Keyword")
        self._keyword = value

    @keyword.deleter
    def keyword(self):
        print("Deleter of keyword")
        del self._keyword

    #GEOCODE
    @property
    def geocode(self):
        print("Geocode property for search")
        return self._geocode

    @geocode.setter
    def geocode(self,value):
        print("Setter of Geocode")
        self._geocode = value

    @geocode.deleter
    def geocode(self):
        print("Deleter of geocode")
        del self._geocode

    #LANG
    @property
    def lang(self):
        print("Lang property for search")
        return self._lang

    @lang.setter
    def lang(self,value):
        print("Setter of Lang")
        self._lang = value

    @lang.deleter
    def lang(self):
        print("Deleter of Lang")
        del self._lang

    #MAX_RESULTS
    @property
    def max_results(self):
        print("Max Results property for search")
        return self._max_results

    @max_results.setter
    def max_results(self,value):
        print("Setter of Max Results")
        self._max_results = value

    @max_results.deleter
    def max_results(self):
        print("Deleter of Max Results")
        del self._max_results

    #MAX_DATE
    @property
    def max_date(self):
        print("Max Date property for search")
        return self._max_date

    @max_date.setter
    def max_date(self,value):
        print("Setter of Max Date")
        self._max_date = value

    @max_date.deleter
    def max_date(self):
        print("Deleter of MAx Date")
        del self._max_date