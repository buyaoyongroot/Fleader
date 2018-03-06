#from Fleader.Get import rq
#主要是方便测试的几个简单的demo
from Fleader.Get import rq
#from lxml import etree
#from pprint import pprint
#import json,re,bs4
#import os


url="http://www.baidu.com/"
rt=rq.get(url)
rq.rw(r"index.html",rt)

'''
soup=bs4.BeautifulSoup(rq,"html.parser")
af=soup.find(attrs={'class':'GridTableContent'}).findAll('tr')

selector=etree.HTML(rt)
content=selector.xpath('//*[@class="full-list-wrap"]/div')

re.findall("a href=\'[a-zA-z]+://[^\s]*prof-sb-browse_map-name",html2)


URLS = ['http://www.cnblogs.com/moodlxs/p/3248890.html', 
        'https://www.zhihu.com/topic/19804387/newest',
        'http://blog.csdn.net/yueguanghaidao/article/details/24281751',
        'https://my.oschina.net/visualgui823/blog/36987',
        'http://blog.chinaunix.net/uid-9162199-id-4738168.html',
        'http://www.tuicool.com/articles/u67Bz26',
        'http://rfyiamcool.blog.51cto.com/1030776/1538367/',
        'http://itindex.net/detail/26512-flask-tornado-gevent']
def get(url):
    r = rs.get(url, timeout=2.0)
rq.pool(get,URLS,100)#get函数 url列表 10,线程数
'''
'''
url="http://2017.ip138.com/ic.asp"
ip138=rq.get(url,proxies={"http": "http://127.0.0.1:1080","https": "http://127.0.0.1:1080"})
ip2=rq.mid(ip138,"[","]")
print(ip2)
'''
'''
txt=''''''#Fiddler info copy
url="https://www.v2ex.com/"
f_headers=rq.f2h(txt)
f_headers["User-Agent"]=rq.rua2()
rt=rq.get(url,headers=f_headers)
rq.rw(r"index.html",rt)
'''
#from Fleader.Plugin.qqwry.qqwry import QQwry
#result = QQwry().lookup('115.196.104.131')
#print(result)




