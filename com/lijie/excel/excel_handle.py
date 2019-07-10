# coding=utf-8
import os
from datetime import datetime

import xlrd
from xlrd import xldate_as_tuple

from com.lijie.oracle.oracle_handle import *

# 解决乱码问题
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


# xlrd.Book.encoding = "gbk"

# ctype： 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
class excelHandle:
    def get_column_type(self, filename, sheetname):
        rbook = xlrd.open_workbook(filename)
        sheet = rbook.sheet_by_name(sheetname)
        rows = sheet.nrows
        cols = sheet.ncols
        for i in range(rows):
            row_content = []
            for j in range(cols):
                ctype = sheet.cell(i, j).ctype  # 表格的
                value = sheet.cell(i, j).value
                print(value, "=", ctype)

    def decode(self, filename, sheetname):
        try:
            filename = filename.decode('utf-8')
            sheetname = sheetname.decode('utf-8')
        except Exception:
            print(traceback.print_exc())
        return filename, sheetname

    def read_excel(self, filename, sheetname):
        # filename, sheetname = self.decode(filename, sheetname)
        rbook = xlrd.open_workbook(filename)
        sheet = rbook.sheet_by_name(sheetname)
        rows = sheet.nrows
        cols = sheet.ncols
        all_content = []
        for i in range(rows):
            row_content = []
            for j in range(cols):
                ctype = sheet.cell(i, j).ctype  # 表格的数据类型
                cell = sheet.cell_value(i, j)
                if ctype == 2 and cell % 1 == 0:  # 如果是整形
                    # cell = int(cell)
                    pass
                elif ctype == 3:
                    # 转成datetime对象
                    date = datetime(*xldate_as_tuple(cell, 0))
                    cell = date.strftime('%Y/%d/%m %H:%M:%S')
                    # cell = "to_date("+date.strftime('%Y/%d/%m %H:%M:%S')+",'yyyy-mm-dd hh24:mi:ss')"
                elif ctype == 4:
                    cell = True if cell == 1 else False
                row_content.append(cell)
            all_content.append(tuple(row_content))
            # print ('[' + ','.join("'" + str(element) + "'" for element in row_content) + ']')
        # del all_content[0]

        return all_content


if __name__ == '__main__':
    eh = excelHandle()
    file_name = r'E:686/3.xlsx'
    sheet_name = 'A库'
    # excel_data = eh.read_excel(file_name, sheet_name)
    # table_name = "cont_test2"
    # connect = oracleHandle.connect("u_db_wx", "u_db_wx", "172.17.209.243:1521/bidbportal")
    # oracleHandle.insert(connect, excel_data, table_name)
    eh.get_column_type(file_name, sheet_name)
