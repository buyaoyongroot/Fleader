import subprocess
def readini(path,rnode,snode):
    import configparser      
    cf = configparser.ConfigParser() 
    cf.read(path)
    txt=cf.get(rnode,snode)
    return str(txt)
'''
def writeini(path,rnode,snode,txt):
    import configparser      
    cf = configparser.ConfigParser()
    cf.read(path)
    cf.set(rnode,snode,txt)
    f=open(path, "w")
    cf.write(f)
    f.close()
'''
username=readini("conf.ini","db","username")
password=readini("conf.ini","db","password")

g_adsl_account = {"name": "宽带连接",
                "username":username,
                "password":password}
class Adsl(object):
    #==============================================================================
    # __init__ : name: adsl名称
    #==============================================================================
    def __init__(self):
        self.name = g_adsl_account["name"]
        self.username = g_adsl_account["username"]
        self.password = g_adsl_account["password"]

    #==============================================================================
    # set_adsl : 修改adsl设置
    #==============================================================================
    def set_adsl(self, account):
        self.name = account["name"]
        self.username = account["username"]
        self.password = account["password"]

    #==============================================================================
    # connect : 宽带拨号
    #==============================================================================
    def connect(self):
        cmd_str = "rasdial %s %s %s" % (self.name, self.username, self.password)
        #print(cmd_str)
        subprocess.call(cmd_str, shell=True)


    #==============================================================================
    # disconnect : 断开宽带连接
    #==============================================================================
    def disconnect(self):
        cmd_str = "rasdial %s /disconnect" % self.name
        #print(cmd_str)
        subprocess.call(cmd_str, shell=True)


    #==============================================================================
    # reconnect : 重新进行拨号
    #==============================================================================
    def reconnect(self):
        self.disconnect()
        self.connect()
