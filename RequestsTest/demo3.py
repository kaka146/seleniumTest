import requests
import traceback
from dbtools import DBTool
from exceltools import read_excel

#1.读取Excel中的测试用例
datas = read_excel("接口测试用例.xlsx", "Sheet1")  #运行

for r in datas:    #datas = [[测试用例1]，[测试用例2]]

    print(r)
    #2.填数据来发请求
    u = r[2] #接口地址
    d = r[3] #数据
    m = r[4] #方法名字/get/post
    h = r[5] #excel定义的状态码
    c = r[6] #返回信息
    n = d["username"] #取用户名
    res = requests.request(m,url=u,json=d) #request方法更加智能，传get用Get
    
    try:
    #断言
        assert res.status_code == h
        assert res.json()["status"] == 200

        #对比数据库
        db = DBTool(host="www.testgoup.com/",username="ljtest",password="a123456",db="ljtestdb")
        sql = "select * from t_user where username='{}'".format(n)
        r = db.query(sql)
        assert r != False   # 为了判断该数据库查询成功，不成功则数据查询失败，代码异常
        assert len(r) != 0   #为了判断数据库里存在这个用户没
        print("测试用例执行成功")
    except Exception as e:
        traceback.print_exc()
        print("测试用例执行失败")

