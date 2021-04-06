"""
    python 读写excel
"""
import xlrd
import requests

def read_excel(excel_path,sheet_name,skip_first=True):
    """
        读取excel方法
        参数: 
            -excel_path:excel的绝对路劲
            -sheet_name:表格的名字
            -skip_first:是否跳过首页：默认的是/false跳过
    """
    result = []
    datas = xlrd.open_workbook(excel_path)  #通过路径打开工作簿
    table = datas.sheet_by_name("Sheet1")  #打开工作簿的表格
  
    if skip_first == True:     #判断是否跳过首页
        start_row = 1
    else:
        start_row = 0

    #循环的读取每一行数据   #nrows 是看表格有多少行
    for row in range(start_row,table.nrows):
        result.append(table.row_values(row))

    return result

# p = "C:\\Users\\kaka\\Desktop\\接口测试用例.xlsx"  #地址
# s = "Sheet1"  #表格名称
# res = read_excel(p, s)  #运行
# for r in res:
#     print(r)