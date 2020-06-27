class DianpingMainCategory:
    def __init__(self, category_id, category_name):
        self._category_id = category_id
        self._category_name = category_name
        # pass

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, id):
        self._category_id = id

    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, name):
        self._category_name = name

    def __str__(self):
        return 'category_id=%d, category_name=%s' % (self._category_id, self._category_name)
