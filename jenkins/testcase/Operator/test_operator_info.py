#coding=utf-8
import unittest, sys, os, requests, json
sys.path.append('..')
sys.path.append(os.path.abspath(os.listdir('..')[0] + '/' +'../../'))
import MySQLdb
from Base.test_CreatePhoneNum import *
from Base.test_CreateChinese import *
class Info(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url = 'http://10.10.100.206/ucenter/operator/info'
        self.Nullphone4 = AutoMysqlPhoneIsOrNo('13700000004')
    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''获取已认证的服务商认证信息'''
        usr=get_IdOrToken(sql(allSql()['sql5'])[0])
        usrId=usr[0]
        usrheader= usr[2]
        content = {'userId':usrId}
        r = requests.get(url=self.url, params=content, headers=usrheader,timeout=5)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''获取认证中的服务商的认证信息'''
        usr = get_IdOrToken(sql(allSql()['sql4'])[0])
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content, headers=usrheader, timeout=5)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_03_allTrue(self):
        '''获取未认证的服务商的认证信息'''
        usr = get_IdOrToken(self.Nullphone4)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content, headers=usrheader, timeout=5)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNone(r.json()['entity'])

if __name__ == '__main__':
    unittest.main()
