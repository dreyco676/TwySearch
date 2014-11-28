from twython import Twython
import urllib.request
import json
from auth import TwitterUser
twitter = TwitterUser()
twitter.read_json()
auth = twitter.auth()
print(twitter._app_key)
#twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


request = auth.search(q='python', result_type='Popular', geocode=None, count=100)

print(len(request["statuses"]))
