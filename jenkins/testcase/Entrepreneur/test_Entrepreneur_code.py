#coding=utf-8
import unittest, sys, os, requests, json
sys.path.append('..')
sys.path.append(os.path.abspath(os.listdir('..')[0] + '/' +'../../'))
import MySQLdb
from Base.test_CreatePhoneNum import *
class Code(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url='http://10.10.100.207:8085/ucenter/ent/invite/code'
        self.phone1 = AutoMysqlPhoneIsOrNo('13700000001')
        self.phone4 = AutoMysqlPhoneIsOrNo('13700000004')
        self.invitephone= AutoMysqlPhoneIsOrNo('15652000003')

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''查询不是被邀请的用户是否包含邀请码'''
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
        '''查询被邀请的用户是否包含邀请码'''
        usr = get_IdOrToken(self.invitephone)
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

    def test_03_allTrue(self):
        '''查询被邀请的用户是usrId为空'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        r = requests.get(url=self.url,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'请求参数不正确')
        self.assertIsNone(r.json()['entity'])

    def test_04_allTrue(self):
        '''查询普通用户是否包含邀请码'''
        usr = get_IdOrToken(self.phone4)
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

if __name__ == '__main__':
    unittest.main()