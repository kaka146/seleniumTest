import requests
import traceback
from dbtools import DBTool 

u = "http://127.0.0.1:2333/login"
d = {"username":"kakkg","password":"12345678"}
res = requests.post(url=u,json=d)
# print(res.text)
try:
    #断言
    assert res.status_code == 200
    # print("状态码正常")
    assert res.json()["status"] == 200 #判断status状态

    #对比数据库
    db = DBTool(host="127.0.0.1",username="root",password="123456",db="ljtestdb")
    sql = "select * from t_user where username='{}'".format(d["username"])
    r = db.query(sql)
    assert r != False   # 为了判断该数据库查询成功，不成功则数据查询失败，代码异常
    assert len(r) != 0   #为了判断数据库里存在这个用户
    print("测试用例执行成功")
except Exception as e:
    traceback.print_exc()
    print("测试用例执行失败")