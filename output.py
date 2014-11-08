import simplejson

class FormatOutput(object):
    def __init__(self):
        #twitter documentation
        #https://dev.twitter.com/rest/reference/get/search/tweets
        self._out_dir = ''
        self._file_name = 'output'
        self._out_type = 'json'
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
    def out_dir(self,value):
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
        simplejson.dump(self._result_set, f)
        f.close()

    def csv_output(self):
        print('#do stuff')