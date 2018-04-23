from configparser import  ConfigParser
import  os


class con():
    def __init__(self):
        self.config=ConfigParser()
        self.configpath=os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.ini')
        self.config.read(self.configpath,encoding='utf-8')
        self.conf={'username':'','passwords':'','db':'','success':''}

    def confset(self):
        self.conf['username']=self.config.get('database','username')
        self.conf['passwords']=self.config.get('database','passwords')
        self.conf['db']=self.config.get('database','db')
        self.conf['success']=self.config.get('code','success')

        return self.conf



if __name__=='__main__':
    c=con()
    print(c.confset())


