class DianpingSubCategory:
    def __init__(self, sub_category_id, main_category_id, sub_category_name):
        self._sub_category_id = sub_category_id
        self._main_category_id = main_category_id
        self._sub_category_name = sub_category_name

    @property
    def sub_category_id(self):
        return self._sub_category_id

    @sub_category_id.setter
    def sub_category_id(self, value):
        self._sub_category_id = value

    @property
    def main_category_id(self):
        return self._main_category_id

    @main_category_id.setter
    def main_category_id(self,value):
        self._main_category_id = value

    @property
    def sub_category_name(self):
        return self._sub_category_name

    @sub_category_name.setter
    def sub_category_name(self,value):
        self._sub_category_name = value

    def __str__(self):
        return 'sub_category_id=%d, main_category_id= %d, sub_category_name=%s'%(self._sub_category_id,self._main_category_id,self._sub_category_name)
