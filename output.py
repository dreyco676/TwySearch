class FormatOutput(object):
    def __init__(self):
        #twitter documentation
        #https://dev.twitter.com/rest/reference/get/search/tweets
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

    def save_json_file(self, out_dir, file_name):
        #do stuff

    def save_delimited_file(self, out_dir, file_name, delimiter):
        #do stuff