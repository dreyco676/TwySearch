import twython

class TwitterSearch:
    def __init__(self, keywords, geocode=None, lang=None, max_results=None, max_date=None):
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

    def convert_params(self):
        param_list = [self.search_params['keywords']]
        if self.search_params['geocode'] is not None:
            param_list.extend('geocode='+str(self.search_params['geocode']))
        if self.search_params['lang'] is not None:
            param_list.extend('lang='+str(self.search_params['lang']))
        if self.search_params['max_results'] is not None:
            param_list.extend('count='+str(self.search_params['max_results']))
        if self.search_params['max_date'] is not None:
            param_list.extend('until='+str(self.search_params['max_date']))

        return param_list

    def page_results(self, max_results):

    def make_request(self):
        if self.search_params.max_results > 100:
            while self.search_params.max_results > 100:
                twython.search(self.search_params)
        else:
            #make request
            twython.search(self.search_params)
