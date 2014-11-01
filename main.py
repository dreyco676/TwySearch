import search
import user


keywords ='polly'
geocode ='US'
lang = 'English'
max_results = 100
max_date = None

s = search.TwitterSearch(keywords, geocode, lang, max_results, max_date)

name = 'John Hogue'
company = 'General Mills'
app_key = '37ZrxAQkWjZi5Mj7euFk0fT2e'
app_secret = 'Bo5duJpMC3iLHeZuOKyIkZJsOoLcnXbnCfURsrawCZPIp908t3'
oauth_token = '39855951-6MtVemzUgai6hQRMOhNVldha8Fa8nAQoNmfmZYqII'
oauth_token_secret = '6I3GlIJ1o4T0DB634KcQRQYghreLkv3jGmeZLIV3Amw68'

a = user.TwitterUser(name, company, app_key, app_secret, oauth_token, oauth_token_secret)

r = search.TwitterRequest(s.get_search_params(),a.get_auth())
