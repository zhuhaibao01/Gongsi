#coding=utf-8
import unittest, sys, os, requests, json
sys.path.append('..')
sys.path.append(os.path.abspath(os.listdir('..')[0] + '/' +'../../'))
import MySQLdb
from Base.test_CreatePhoneNum import *
from Base.test_CreateChinese import *
class volidate(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url = 'http://10.10.100.206/ucenter/operator/volidate'

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''对未通过的服务商营业执照进行验证'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[1])
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        content = {'licenseNo':'123456789012345687','userId':usrId}
        r = requests.get(url=self.url, params=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertEqual(r.json()['entity'],True)

    def test_02_allTrue(self):
        '''对已通过的服务商商营业执照进行验证'''
        usr = get_IdOrToken(18600000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'licenseNo': '123456789012345678', 'userId': usrId}
        r = requests.get(url=self.url, params=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],17003)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'该企业已被认证，请重新填写')
        self.assertIsNone(r.json()['entity'],)

if __name__ == '__main__':
    unittest.main()
