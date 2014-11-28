import json
import csv
import re

class FormatOutput(object):
    def __init__(self):
        #twitter documentation
        #https://dev.twitter.com/rest/reference/get/search/tweets
        self._out_dir = ''
        self._file_name = 'output'
        self.delimiter = 'json'
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

    #OUT_DIR
    @property
    def out_dir(self):
        return self._out_dir

    @out_dir.setter
    def out_dir(self,value):
        self._out_dir = value

    @out_dir.deleter
    def out_dir(self):
        del self._out_dir

    #FILE_NAME
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self,value):
        self._file_name = value

    @file_name.deleter
    def file_name(self):
        del self._file_name

    #OUT_TYPE
    @property
    def out_type(self):
        return self._out_type

    @out_type.setter
    def out_type(self,value):
        self._out_type = value

    @out_type.deleter
    def out_type(self):
        del self._out_type

    def json_output(self):
        name = self._out_dir + self._file_name + "." + self._out_type
        f = open(name, "w")
        json.dump(self._result_set, f, indent=4)
        f.close()

    def tsv_output(self):
        name = self._out_dir + self._file_name + "." + self._out_type
        with open(name, "w+",encoding='utf-8') as the_file:
            writer = csv.writer(the_file, delimiter='\t', lineterminator='\n')
            data = self._result_set
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
