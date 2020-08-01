import xlrd
import xlwt
from xlutils.copy import copy


class XlsUtil():
    '''
    execl操作工具类
    '''

    def path_is_exist(self, path):
        '''
        判断是否存在工作簿
        :param path: 工作簿名称
        :return: 存在 返回True; 不存在 返回False
        '''
        try:
            xlrd.open_workbook(path, formatting_info=True)
        except FileNotFoundError as e:
            return False
        return True

    def sheet_name_is_exist(self, path, sheet_name):
        '''
        判断是否存在表名
        :param path: 工作簿
        :param sheet_name: 表名
        :return: 存在工作簿和表名 返回True； 否则 返回False
        '''
        path_exist = self.path_is_exist(path)
        if path_exist:
            workbook = xlrd.open_workbook(path)  # 打开工作簿
            sheets = workbook.sheet_names()
            if sheet_name in sheets:
                return True
        return False

    def create_a_sheet(self, path, sheet_name, value):
        '''
        创建一张表
        :param path: 工作簿
        :param sheet_name: 表名
        :param value: 表头
        :return: 存在工作簿 存在表名 创建失败 返回False; 存在工作簿 不存在表名 创建成功 返回True； 不存在工作簿 创建成功 返回True
        '''
        if self.path_is_exist(path):
            workbook = xlrd.open_workbook(path, formatting_info=True)
            if self.sheet_name_is_exist(path, sheet_name):
                print(f'表名为[{sheet_name}]已经才在[{path}]中')
                return False
            else:
                index = len(value)
                wb = copy(workbook)
                # add sheet to workbook with existing sheets
                sheet = wb.add_sheet(sheet_name)
                for i in range(0, index):
                    for j in range(0, len(value[i])):
                        sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
                wb.save(path)  # 保存工作簿
                print("xls格式表格写入数据成功！")
                return True
        else:
            index = len(value)  # 获取需要写入数据的行数
            workbook = xlwt.Workbook()  # 新建一个工作簿
            sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
            for i in range(0, index):
                for j in range(0, len(value[i])):
                    sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
            workbook.save(path)  # 保存工作簿
            print("xls格式表格写入数据成功！")
            return True

    def sheet_append_data(self, path, sheet_name, value):
        '''
        向一张表中追加数据
        :param path: 工作簿
        :param sheet_name: 表名
        :param value: 数据
        :return:
        '''
        if self.path_is_exist(path):
            if self.sheet_name_is_exist(path, sheet_name):
                index = len(value)  # 获取需要写入数据的行数
                workbook = xlrd.open_workbook(path)  # 打开工作簿
                sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
                worksheet = workbook.sheet_by_name(sheet_name)  # 获取工作簿中所有表格中的的第一个表格
                rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
                new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
                new_worksheet = new_workbook.get_sheet(sheet_name)  # 获取转化后工作簿中的第一个表格
                for i in range(0, index):
                    for j in range(0, len(value[i])):
                        new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
                new_workbook.save(path)  # 保存工作簿
                print(f"[{sheet_name}]表格【追加】写入数据成功！")
            else:
                print(f'[{sheet_name}]表不存在！')
        else:
            print(f'[{path}]工作簿不存在！')

    def sheet_read(self, path, sheet_name):
        '''
        输出指定表的数据
        :param path: 工作簿
        :param sheet_name:表
        :return:
        '''
        if self.path_is_exist(path):
            if self.sheet_name_is_exist(path, sheet_name):
                workbook = xlrd.open_workbook(path)  # 打开工作簿
                # sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
                worksheet = workbook.sheet_by_name(sheet_name)  # 获取工作簿中所有表格中的的第一个表格
                for i in range(0, worksheet.nrows):
                    for j in range(0, worksheet.ncols):
                        print(worksheet.cell_value(i, j), "\t", end="")  # 逐行逐列读取数据
                    print()
            else:
                print(f'[{sheet_name}]表不存在！')
        else:
            print(f'[{path}]工作簿不存在！')


xls_util = XlsUtil()
book_name = '测试工作簿.xls'

sheet_name = '测试表3'

value_title = [["姓名", "性别", "年龄", "城市", "职业"], ]

value1 = [["张三", "男", "19", "杭州", "研发工程师"],
          ["李四", "男", "22", "北京", "医生"],
          ["王五", "女", "33", "珠海", "出租车司机"], ]

value2 = [["Tom", "男", "21", "西安", "测试工程师"],
          ["Jones", "女", "34", "上海", "产品经理"],
          ["Cat", "女", "56", "上海", "教师"], ]


def main():
    xls_util.create_a_sheet(book_name, sheet_name, value_title)
    xls_util.sheet_append_data(book_name, sheet_name, value1)
    xls_util.sheet_append_data(book_name, sheet_name, value2)
    xls_util.sheet_read(book_name, sheet_name)


if __name__ == '__main__':
    main()
