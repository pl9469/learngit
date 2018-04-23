from configparser import  ConfigParser


config=ConfigParser()
config.add_section('database')
config.set('database','username','hbgms_v2_test')
config.set('database','passwords','test')
config.set('database','db','HBGMS19')
config.add_section('code')
config.set('code','success','0')


config.write(open('config.ini','w'))



