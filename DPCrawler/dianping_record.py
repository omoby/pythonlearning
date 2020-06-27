class DianpingRecord:
    def __init__(self,row_key,region_id,sub_category_id,recod_num):
        self._row_key = row_key
        self._region_id = region_id
        self._sub_category_id = sub_category_id
        self._record_num = recod_num

    @property
    def row_key(self):
        return self._row_key

    @row_key.setter
    def row_key(self,row_key):
        self._row_key = row_key

    @property
    def region_id(self):
        return self._region_id

    @region_id.setter
    def region_id(self,region_id):
        self._region_id = region_id

    @property
    def sub_category_id(self):
        return self._sub_category_id

    @sub_category_id.setter
    def sub_category_id(self,sub_category_id):
        self._sub_category_id = sub_category_id

    @property
    def record_num(self):
        return self._record_num

    @record_num.setter
    def record_num(self,record_num):
        self._record_num = record_num

    def __str__(self):
        return 'row_key=%s, region_id=%d, sub_category_id=%d, record_num=%d '%(self._row_key,self._region_id,self._sub_category_id,self._record_num)