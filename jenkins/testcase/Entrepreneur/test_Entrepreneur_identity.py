#coding=utf-8
import unittest, sys, os, requests, json
sys.path.append('..')
sys.path.append(os.path.abspath(os.listdir('..')[0] + '/' +'../../'))
import MySQLdb
from Base.test_CreatePhoneNum import *
class Code(unittest.TestCase):
    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url = 'http://10.10.100.206/ucenter/ent/authentication/identity'
        self.phone1 = AutoMysqlPhoneIsOrNo('13700000001')
        self.phone4 = AutoMysqlPhoneIsOrNo('13700000004')
        self.identyphone = AutoMysqlPhoneIsOrNo('15652000003')


    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''获取法人身份认证信息接口'''
        # usr = get_IdOrToken(15652000002)
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId':usrId}
        r = requests.get(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''获取普通用户身份认证信息接口'''
        # usr = get_IdOrToken(15652000002)
        usr = get_IdOrToken(self.phone4)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 15001)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'当前用户不存在企业主信息，请认证企业主信息')
        self.assertIsNone(r.json()['entity'])

    def test_03_allTrue(self):
        '''获取代理人身份认证信息接口'''
        usr = get_IdOrToken(self.identyphone)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId':usrId}
        r = requests.get(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_04_allTrue(self):
        '''userId为空'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        r = requests.get(url=self.url, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'请求参数不正确')
        self.assertIsNone(r.json()['entity'])

if __name__ == '__main__':
    unittest.main()