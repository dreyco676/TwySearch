__author__ = 'dreyco676'

import csv
import re
from twython import Twython
import json
import time
import sys
import datetime
import math
import os.path

class TwitterUser:
    def __init__(self):
        self._app_key = None
        self._app_secret = None
        self._oauth_token = None
        self._oauth_token_secret = None

    #APP_KEY
    @property
    def app_key(self):
        return self._app_key

    @app_key.setter
    def app_key(self, value):
        self._app_key = value

    @app_key.deleter
    def app_key(self):
        del self._app_key

    #APP_SECRET
    @property
    def app_secret(self):
        return self._app_secret

    @app_secret.setter
    def app_secret(self, value):
        self._app_secret = value

    @app_secret.deleter
    def app_secret(self):
        del self._app_secret

    #OAUTH_TOKEN
    @property
    def oauth_token(self):
        return self._oauth_token

    @oauth_token.setter
    def oauth_token(self, value):
        self._oauth_token = value

    @oauth_token.deleter
    def oauth_token(self):
        del self._oauth_token

    #OAUTH_TOKEN_SECRET
    @property
    def oauth_token_secret(self):
        return self._oauth_token_secret

    @oauth_token_secret.setter
    def oauth_token_secret(self, value):
        self._oauth_token_secret = value

    @oauth_token_secret.deleter
    def oauth_token_secret(self):
        del self._oauth_token_secret

    def read_app_json(self):
        #read the application credentials
        json_data = open('app_auth.json')
        data = json.load(json_data)
        self.app_key = data["app_key"]
        self.app_secret = data["app_secret"]
        json_data.close()

    def auth_url(self):
        self.read_app_json()
        #get auth url from twitter
        twitter = Twython(self.app_key, self.app_secret)
        auth = twitter.get_authentication_tokens()
        #set oauth token
        self.oauth_token = auth["oauth_token"]
        self.oauth_token_secret = auth["oauth_token_secret"]
        url = auth['auth_url']
        return url

    def save_user(self, oauth_verifier):
        twitter = self.auth()
        user_cred = twitter.get_authorized_tokens(oauth_verifier)
        with open('user_auth.json', 'w+') as outfile:
          json.dump(user_cred, outfile)

    def read_user_json(self):
        json_data = open('user_auth.json')
        data = json.load(json_data)
        self.oauth_token = data["oauth_token"]
        self.oauth_token_secret = data["oauth_token_secret"]
        json_data.close()

    def new_user(self):
        if os.path.isfile('user_auth.json'):
            return False
        else:
            return True

    def auth(self):
        self.read_app_json()
        twitter_auth = Twython(self.app_key, self.app_secret, self.oauth_token, self.oauth_token_secret)
        return twitter_auth




class TwitterOutput(object):
    def __init__(self):
        #twitter documentation
        #https://dev.twitter.com/rest/reference/get/search/tweets
        self._file_name = 'output.tsv'
        self._result_set = None

    #RESULT_SET
    @property
    def result_set(self):
        return self._result_set

    @result_set.setter
    def result_set(self,value):
        self._result_set = value

    @result_set.deleter
    def result_set(self):
        del self._result_set

    #FILE_NAME
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self,value):
        if value is None:
            self._file_name = 'Output.tsv'
        else:
            self._file_name = value

    @file_name.deleter
    def file_name(self):
        del self._file_name

    def json_output(self):
        name = self.file_name
        f = open(name, "w+")
        json.dump(self.result_set, f, indent=4)
        f.close()

    def tsv_output(self):
        name = self.file_name
        with open(name, "w+",encoding='utf-8') as the_file:
            writer = csv.writer(the_file, delimiter='\t', lineterminator='\n')
            header = ['tweetID','timeCreatedUTC','timeOffset','tweetText','favoriteCount','retweetCount','language',
                             'place','twitterHandle','accountLocation','accountName','source','geoCoords']
            writer.writerow(header)
            data = self.result_set
            for tweetObject in data:
                try:
                    timeCreatedUTC = tweetObject["created_at"]
                except:
                    timeCreatedUTC = None
                try:
                    favoriteCount = tweetObject["favorite_count"]
                except:
                    favoriteCount = 0
                try:
                    geoCoords = tweetObject["coordinates"]
                except:
                    geoCoords = None
                try:
                    tweetID = tweetObject["id"]
                except:
                    tweetID = None
                try:
                    retweetCount = tweetObject["retweet_count"]
                except:
                    retweetCount = 0
                try:
                    source = tweetObject["source"]
                except:
                    source = None
                try:
                    tweetText = re.sub('\s+',' ',tweetObject["text"])
                except:
                    tweetText = None
                try:
                    language = tweetObject["lang"]
                except:
                    language = None
                try:
                    place = tweetObject["place"]
                except:
                    place = None
                try:
                    timeOffset = tweetObject["user"]["utc_offset"]
                except:
                    timeOffset = None
                try:
                    twitterHandle = tweetObject["user"]["screen_name"]
                except:
                    twitterHandle = None
                try:
                    accountLocation = tweetObject["user"]["lang"]
                except:
                    accountLocation = None
                try:
                    accountName = re.sub('\s+',' ',tweetObject["user"]["name"])
                except:
                    accountName = None
                tweetData = [tweetID,timeCreatedUTC,timeOffset,tweetText,favoriteCount,retweetCount,language,
                             place,twitterHandle,accountLocation,accountName,source,geoCoords]
                writer.writerow(tweetData)

class TwitterRequest(object):
    def __init__(self):
        self._keyword = None
        self._geocode = None
        self._lang = None
        self._result_type = None
        self._max_results = None
        self._max_date = None
        self._session = None
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
        if len(value) == 0:
            self._geocode = None
        else:
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
        if value == 'None':
            self._lang = None
        else:
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
        try:
            self._max_results = int(value)
        except:
            self._max_results = 15

    @max_results.deleter
    def max_results(self):
        del self._max_results

    #MAX_DATE
    @property
    def max_date(self):
        return self._max_date

    @max_date.setter
    def max_date(self,value):
        if len(value) == 0:
            self._max_date = None
        else:
            self._max_date = value

    @max_date.deleter
    def max_date(self):
        del self._max_date

    #SESSION
    @property
    def session(self):
        return self._session

    @session.setter
    def session(self,value):
        self._session = value

    @session.deleter
    def session(self):
        del self._session

    def make_request(self):
        #for paging read tweets older than max_id
        max_id = None
        data = {}
        if self.max_results > 100:
            while self.max_results > 100:
                start_time = datetime.datetime.now()
                request = self.session.search(q=self.keyword, geocode=self.geocode, lang=self.lang,
                                    result_type=self.result_type, count=100, until=self.max_date, max_id=max_id)
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
                    count_returned = sys.maxsize
                self.max_results -= count_returned

                #Rate Handling
                #twitter rate limits at 180/15min = 1/5sec
                end_time = datetime.datetime.now()
                elapsed_sec = (end_time - start_time).total_seconds()
                time.sleep(5 - elapsed_sec)

        #make request that is >=100
        request = self.session.search(q=self.keyword, geocode=self.geocode, lang=self.lang,
                                result_type=self.result_type, count=self.max_results, until=self.max_date, max_id=max_id)
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
        num_requests = math.ceil(self.max_results / max_call_results)
        api_rate = 5
        estimate_completion = num_requests * api_rate
        return estimate_completion