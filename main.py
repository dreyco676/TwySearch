from search import TwitterSearch
from twython import Twython
from request import TwitterRequest
from output import FormatOutput

APP_KEY = '37ZrxAQkWjZi5Mj7euFk0fT2e'
APP_SECRET = 'Bo5duJpMC3iLHeZuOKyIkZJsOoLcnXbnCfURsrawCZPIp908t3'
OAUTH_TOKEN = '39855951-6MtVemzUgai6hQRMOhNVldha8Fa8nAQoNmfmZYqII'
OAUTH_TOKEN_SECRET = '6I3GlIJ1o4T0DB634KcQRQYghreLkv3jGmeZLIV3Amw68'
twitter_auth = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


search = TwitterSearch()
search.keyword ='Python'
search.max_results = 5

req = TwitterRequest()
req._req_param = search
req._session_auth = twitter_auth
data = req.make_request()

save = FormatOutput()
save._file_name = 'Output'
save._out_type = 'json'
save._result_set = data
save.json_output()