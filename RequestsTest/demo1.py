#接口自动化测试 requests 第三方的包

#1、导入requests
import  requests

# url = "http://www.baidu.com/"   #请求的网址/接口
# res = requests.get(url)         #requests。get(url)> response(响应头body)用requests的get方法去请求这个网址
# print(res.text)                 #打印响应的信息 show
#请求测谈网的地址
url = "https://www.testgoup.com/showversion"
res = requests.get(url)   

#http状态码：判断接口能不能工作
#断言：如果表达式成立=断言通过/不成功就包错
assert res.status_code == 200
# print(res.status_code) #获取http状态
print("状态码正常")

# #判断该接口功能是否正常
r = res.json() #把返回值变成字典

assert r.get("status") == 200
print("接口测试通过")


