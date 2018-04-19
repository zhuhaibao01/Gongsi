#coding=utf-8
import unittest, sys, os, requests
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from test_CreatePhoneNum import *

class member_getBeInvitedStatus(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url='http://10.10.100.206/ucenter/invited/getBeInvitedStatus'
        self.noRegphone = int(C(sql(allSql()['sql1'])))
        self.Smphone='13700000004'
        self.Erphone='13919273370'
        self.Parnerphone='13700000088'
        self.Operatorphone='15652002619'
        self.HEphone='13700000008'

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''查询被邀请人信息为未注册用户'''
        content= {'mobile':self.noRegphone}
        r = requests.get(url=self.url, params=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''查询被邀请人信息为普通首媒用户'''
        content= {'mobile':self.Smphone}
        r = requests.get(url=self.url, params=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_03_allTrue(self):
        '''查询被邀请人信息为企业主'''
        content1 = {'mobile':self.Erphone}
        r = requests.get(url=self.url, params=content1)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_04_allTrue(self):
        '''查询被邀请人信息为新媒人'''
        content1 = {'mobile': self.Parnerphone}
        r = requests.get(url=self.url, params=content1)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_05_allTrue(self):
        '''查询被邀请人信息为服务商'''
        content1 = {'mobile': self.Operatorphone}
        r = requests.get(url=self.url, params=content1)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_06_allTrue(self):
        '''查询被邀请人信息为新媒人和企业主'''
        content1 = {'mobile': self.HEphone}
        r = requests.get(url=self.url, params=content1)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

if __name__=='__main__':
    unittest.main()