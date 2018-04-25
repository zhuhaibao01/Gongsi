#coding=utf-8
import sys,unittest,requests,random
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *

class member_memberEntrance(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url = 'http://10.10.100.206/ucenter/member/memberEntrance'
    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''userId为已存在'''
        usr = get_IdOrToken('15652002619')
        usrId = usr[0]
        usrheader = usr[2]
        content1 = {'userId':usrId}
        r = requests.get(url=self.url, params=content1, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_02_userIdNull(self):
        '''userId为不存在'''
        usr = get_IdOrToken('15652002619')
        usrId = usr[0]
        usrheader = usr[2]
        content1 = {'userId': 9999999}
        r = requests.get(url=self.url, params=content1, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 400)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"用户验证失败")
        self.assertIsNone(r.json()['entity'])

    def test_03_allTrue(self):
        '''userId为空'''
        usr = get_IdOrToken('15652002619')
        usrId = usr[0]
        usrheader = usr[2]
        r = requests.get(url=self.url, headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请求参数不正确")
        self.assertIsNone(r.json()['entity'])

if __name__=='__main__':
    unittest.main()