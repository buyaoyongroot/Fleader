#python3
#make:kele email:kele@masong.me
import requests
import random
import string
import warnings,configparser
warnings.filterwarnings("ignore")
class rq: 
    @staticmethod  
    def get_encode(response):
        rxt=response.text
        encodings = requests.utils.get_encodings_from_content(rxt)
        if encodings:
            return encodings[0]
        else:
            return response.apparent_encoding
    @staticmethod
    def get(url,data="",cookie="",proxies="",timeout=60,headers="",files=""):
        #header_s = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'}
        header_s = {"User-Agent":rq.rua2()}
        if headers!="":
            header_s.update(headers)
        if cookie!="":
            header_s['cookie']=cookie
        if data=="":
            response=requests.get(url,headers=header_s,proxies=proxies,timeout = timeout,verify=False)
        elif data==False:
            response=requests.post(url,headers=header_s,proxies=proxies,timeout=timeout,files=files,verify=False)
        else:
            response=requests.post(url,headers=header_s,proxies=proxies,data=data,timeout=timeout,files=files,verify=False)   
        if response.status_code==200:
            encode=rq.get_encode(response)
            if(encode):
                response.encoding=encode
            return response.text
        else:
            return ""
    def sget(s=requests.Session(),url="",data="",cookie="",timeout=60,headers="",files=""):
        #header_s = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'}
        header_s = {"User-Agent":rq.rua2()}
        if headers!="":
            header_s.update(headers)
        if cookie!="":
            header_s['cookie']=cookie
        if data=="":
            response=s.get(url,headers=header_s,timeout = timeout,verify=False)
        elif data==False:
            response=s.post(url,headers=header_s,timeout=timeout,files=files,verify=False)
        else:
            response=s.post(url,headers=header_s,data=data,timeout=timeout,files=files,verify=False)   
        if response.status_code==200:
            encode=rq.get_encode(response)
            if(encode):
                response.encoding=encode
            return response.text
        else:
            return ""
    @staticmethod        
    def rw(path, line="", aw='a',sp=""):
        if line == "":
            arr = []
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    for l in f:
                        if sp=="":
                            arr.append(l.replace("\n", ""))
                        else:
                            arr.append(l.replace("\n", "").split(sp))                           
            except:
                with open(path, 'r', encoding='gb2312') as f:
                    for l in f:
                        if sp=="":
                            arr.append(l.replace("\n", ""))
                        else:
                            arr.append(l.replace("\n", "").split(sp)) 
            return arr
        else:
            with open(path, aw, encoding='utf-8') as f:
                f.write(line + "\n")
    @staticmethod
    def f2h(txt):
        arr=txt.split("\n")
        headers={}
        for i in arr:
            if ":" in i:
                ic=i.split(": ")
                headers[ic[0].replace("\t","").replace(" ","")]=ic[1]
        return headers
    @staticmethod
    def mid(sStr1,sStr2,sStr3):
        sStrtemp=sStr1[sStr1.find(sStr2)+len(sStr2):len(sStr1)]
        return  sStrtemp[0:sStrtemp.find(sStr3)]
    @staticmethod
    def rs(cc):
        return ''.join(random.sample(string.ascii_letters + string.digits, int(cc)))
    @staticmethod
    def rua():
        from fake_useragent import UserAgent
        ua=UserAgent()
        return ua.random
    @staticmethod
    def wc(list, weight):
        new_list = []
        for i, val in enumerate(list):
            for i in range(weight[i]):
                new_list.append(val) 
        return random.choice(new_list)
    @staticmethod
    def rua2(lang="zh-CN"):
        #最新浏览器随机useragent
        user_agent_list = [
            'Mozilla/5.0 (Windows NT {WindowsNT};{WOW64}{language} rv:{Firefox}) Gecko/{builddata} Firefox/{Firefox}'.format(
            **{'WindowsNT': rq.wc(["6.1","6.2","6.3","10.0"],[3,2,2,3]),'WOW64':rq.wc([""," WOW64;"," Win64;"," x64;"],[3,4,2,1]),'language':rq.wc([""," {};".format(lang)],[6,4]),'builddata':random.choice(["201{}0{}{}".format(random.randint(0, 6),random.randint(1, 9), random.randint(10, 28))]), 'Firefox': random.choice(["50.0.1","50.0.2","50.0","50.01","50.010","50.011","50.02","50.03","50.04","50.05","50.06","50.07","50.08","50.09","50.1.0","51.0.1","51.0","51.01","51.010","51.011","51.012","51.013","51.014","51.02","51.03","51.04","51.05","51.06","51.07","51.08","51.09","52.0.1","52.0.2","52.0","52.01","52.02","52.03","52.04","52.05","52.06","52.07","52.08","52.09","52.1.0","52.1.1","52.1.2","52.2.0","52.2.1","52.3.0","52.4.0","52.4.1","53.0.2","53.0.3","53.0","53.01","53.010","53.02","53.03","53.04","53.05","53.06","53.07","53.08","53.09","54.0.1","54.0","54.01","54.010","54.011","54.012","54.013","54.02","54.03","54.04","54.05","54.06","54.07","54.08","54.09","55.0.1","55.0.2","55.0.3","55.0","55.01","55.010","55.011","55.012","55.013","55.02","55.03","55.04","55.05","55.06","55.07","55.08","55.09","56.0.1","56.0","56.01","56.010","56.011","56.012","56.02","56.03","56.04","56.05","56.06","56.07","56.08","56.09","57.03","57.04","57.05","57.06"]), }),
            'Mozilla/5.0 (Windows NT {WindowsNT};{WOW64}{language}) AppleWebKit/{Safari} (KHTML, like Gecko) Chrome/{Chrome} Safari/{Safari}'.format(
            **{'WindowsNT': rq.wc(["6.1","6.2","6.3","10"],[3,2,2,3]),'WOW64':rq.wc([""," WOW64;"," Win64;"," x64;"],[3,4,2,1]),'language':rq.wc([""," {};".format(lang)],[6,4]), 'Chrome': '{0}.{1}.{2}.{3}'.format(random.randint(50, 61), random.randint(0, 9), random.randint(1000, 9999), random.randint(10, 99)), 'Safari': '{0}.{1}'.format(random.randint(100, 999), random.randint(0, 99)), }),
            'Mozilla/5.0 ({compatible}Windows NT {WindowsNT};{WOW64} MSIE {ie}.0; Trident/{Trident}.0;){Gecko}'.format(
            **{'compatible':random.choice(["","compatible; "]),'WindowsNT': rq.wc(["6.1","6.2","6.3","10"],[3,2,2,3]),'WOW64':rq.wc([""," WOW64;"," Win64;"," x64;"],[3,4,2,1]),'ie': random.randint(10, 11),'Trident': random.randint(5, 7),'Gecko':random.choice([""," like Gecko;"]) }),
            'Mozilla/5.0 (Windows NT {WindowsNT}; MSIE 9.0;) Opera {opera1}.{opera2}'.format(
            **{'WindowsNT': rq.wc(["6.1","6.2","6.3","10"],[3,2,2,3]),'opera1': random.randint(10, 12),'opera2': random.randint(10, 99) }),
           ]
        rs=rq.wc(user_agent_list, [2, 4, 3, 1])#201706 chrome63 firefox14 ie9 opera2
        return rs
    
    @staticmethod
    def rwini(path,rnode,snode,txt=""):
        import configparser      
        cf = configparser.ConfigParser()
        try:
            cf.read(path)
        except:
            cf.readfp(open(path, 'r', encoding='utf-8'))
        if txt=="":
            txt=cf.get(rnode,snode)
            return str(txt)
        else:
            cf.set(rnode,snode,txt)
            f=open(path, "w")
            cf.write(f)
            f.close()            

    @staticmethod
    def wimg(path,content):
        fp = open(path,"wb")
        fp.write(content)
        fp.close()
        
    @staticmethod
    def u2f(url,path):
        header_s = {"User-Agent":rq.rua2()}
        content=requests.get(url,headers=header_s,stream=True,verify=False,timeout=60).content
        fp = open(path,"wb")
        fp.write(content)
        fp.close()
                
    @staticmethod
    def var(arr,var):
        if var in arr:
            return arr[var]
        else:
            return ""
    
    @staticmethod
    def csv(path, line=[], aw='a',f=""):
        import csv
        with open(path,aw,encoding="utf-8") as datacsv:
             if f=="":
                 csvwriter = csv.writer(datacsv,dialect = ("excel"))
             else:
                 csvwriter = csv.writer(datacsv,dialect = ("excel"),delimiter=f)
             csvwriter.writerow(line)

    @staticmethod
    def mk(path):
        import os
        if not os.path.exists(path):
            #os.mkdir(path)
            os.makedirs(path)

    @staticmethod
    def pool(get, URLS,threadNum=10):
        import threadpool         
        pool = threadpool.ThreadPool(threadNum) 
        requests = threadpool.makeRequests(get, URLS) 
        [pool.putRequest(req) for req in requests] 
        pool.wait() 
