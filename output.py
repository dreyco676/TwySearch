from twitter import TwitterOutput

class Output(object):
    def __init__(self):
        self._out_dir = ''
        self._file_name = 'output'
        self._out_type = 'json'
        self._result_set = None
        self._platform = None

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

    #PLATFORM
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self,value):
        self._platform = value

    @platform.deleter
    def platform(self):
        del self._platform


    def format_output(self):
        if self._platform == 'Twitter':
            twitter = TwitterOutput()
            twitter.out_dir = self._out_dir
            twitter.file_name = self._file_name
            twitter.out_type = self._out_type
            twitter.result_set = self._result_set

            if self._out_type == 'json':
                twitter.json_output()
            elif self._out_type == 'tsv':
                twitter.tsv_output()
            else:
                print("Only .tsv and .json are supported at this time.")
        else:
            print("Only Twitter is supported at this time.")