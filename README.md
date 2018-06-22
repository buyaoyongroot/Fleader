### Fleader
pythonic requests ,http请求库

流程
```
函数->参数构造器->文件缓存区->http请求器->编码处理器->文本处理器
```

函数分类
请求类
文件类
文本处理类
数据处理类
并发类
校验类
随机类
工具类
时间类
类型转换类

安装
```
pip install fleader
```

使用
可自动识别url 
```
from fleader import fleader as rq
rt=rq.get('http://www.runoob.com/')
print(rt)
```

参数
```
get(url,data='',cookie='',ip='',timeout=60,headers='',files='',session='',ex='',rw='',cache='')
```

缓存机制
```
rt=rq.get('http://www.runoob.com/',cache=True)
```

不同的文本处理器ex=('jq','xpath','bs4')
```
_,doc=rq.get('http://www.runoob.com/',ex='jq')
item = doc('.item-top,.item-1').items()
for i in item:
	print(i.attr('class'))
	print(i('h4').text())
	print('==========================')
```

并发测试
```
def Downloader(arg):
    q,lock=arg['arg']
    while 1:
        lock.acquire()
        if not q.empty():
            url=q.get()
            lock.release()
            rq.get(url)
        else:
            lock.release()
            break

if __name__ == "__main__":
    urls=['http://127.0.0.1']*100
    q,lock = rq.Manager()
    rq.feed(q,urls)
    rq.sPool(Downloader,tnum=25,cnum=4,arg=[q,lock])
```
