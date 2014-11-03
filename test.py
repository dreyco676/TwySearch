from twython import Twython
import urllib.request
import json
APP_KEY = '37ZrxAQkWjZi5Mj7euFk0fT2e'
APP_SECRET = 'Bo5duJpMC3iLHeZuOKyIkZJsOoLcnXbnCfURsrawCZPIp908t3'
OAUTH_TOKEN = '39855951-6MtVemzUgai6hQRMOhNVldha8Fa8nAQoNmfmZYqII'
OAUTH_TOKEN_SECRET = '6I3GlIJ1o4T0DB634KcQRQYghreLkv3jGmeZLIV3Amw68'
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


request = twitter.search(q='python', result_type='Popular', geocode=None, count=100)

print(request["statuses"])
