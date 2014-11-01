class transform:
    def __init__(self,data, trans_type):
        self.data = data
        self.trans_type = trans_type

class output:
    def __init__(self,data,file_type,filename,out_dir):
        self.data = data
        self.file_type = file_type
        self.filename = filename
        self.out_dir = out_dir
