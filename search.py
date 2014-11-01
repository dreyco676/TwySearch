import twython

class TwitterSearch:
    def __init__(self, keywords, geocode, lang, max_results, max_date):
        #twitter documentation
        #https://dev.twitter.com/rest/reference/get/search/tweets
        self.keywords = keywords
        self.geocode = geocode
        self.lang = lang
        self.max_results = max_results
        self.max_date = max_date

    def get_search_params(self):
        search_params = {'keywords': self.keywords, 'geocode': self.geocode,
                         'lang':self.lang, 'max_results': self.max_results, 'max_date':self.max_date}
        return search_params

class TwitterRequest:
    def __init__(self, search_params, session_auth):
        #twitter documentation
        #https://dev.twitter.com/rest/reference/get/search/tweets
        self.search_params = search_params
        self.session_auth = session_auth

    def page_results(self, max_results):

    def make_request(self):
        if self.search_params.max_results > 100:
            page_results(self.search_params.max_results)
            #do stuff to page


