from fleader import fleader as rq


# _,doc=rq.get('http://www.runoob.com/',ex='jq')
# item = doc('.item-top,.item-1').items()
# for i in item:
# 	print(i.attr('class'))
# 	print(i('h4').text())
# 	print('==========================')



#并发测试
# def Downloader(arg):
#     q,lock=arg['arg']
#     while 1:
#         lock.acquire()
#         if not q.empty():
#             url=q.get()
#             lock.release()
#             rq.get(url)
#         else:
#             lock.release()
#             break

# if __name__ == "__main__":
#     urls=['http://127.0.0.1']*100
#     q,lock = rq.Manager()
#     rq.feed(q,urls)
#     rq.sPool(Downloader,tnum=25,cnum=4,arg=[q,lock])
 



