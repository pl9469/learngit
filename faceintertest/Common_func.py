# -*- coding:utf-8 -*-
import cx_Oracle
import sys

sys.path.append(r'F:\project')
from config.config_init import con
import requests
import json


def db_get():
    '''初始化数据'''
    c = con().confset()
    uname = c['username']
    pswd = c['passwords']
    db = c['db']

    '''连接数据库'''
    dsn = cx_Oracle.makedsn('192.168.187.19', '1521', db)
    conn = cx_Oracle.connect(uname, pswd, db)
    cur = conn.cursor()
    sql = 'select * from  sys_department'
    cur.execute(sql)
    department = cur.fetchall()


    # '''将数据库中表的列名显示'''
    # index=cur.description
    # deslist=[]
    # wardlist=[]
    # for row  in index:
    #    deslist.append(row[0])
    # for line in department:
    #     tmp=zip(deslist,line)
    #     wardlist.append(dict(tmp))
    #
    # print(wardlist)

    '''关闭数据库'''
    cur.close()
    conn.close()
    return department


def get_ward():
    '''传参设置'''
    datainfo = {
        'pageNumer': '1',
        'pageSize': '10',
        '-': '1523442923810'
    }
    '''发送请求'''
    r = requests.post('http://192.168.187.18:7004/framework/web/system/getDeptPageList', data=datainfo)
    result = json.loads(r.text)
    datalist= result['sysDeptDataList']




    return result


if __name__ == '__main__':
    data = db_get()
    ward = get_ward()
