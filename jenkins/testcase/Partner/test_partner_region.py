#coding=utf-8
import sys,unittest,requests
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
class partner_region(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url = 'http://10.10.100.206/ucenter/member/partner/get/region'

    def test_01_allValues(self):
        '''id和区域第一级,第二级，第三级代码均正确'''
        usr = get_IdOrToken('15652002619')
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId':usrId, 'parentCode':0}
        r = requests.get(url=self.url, params=content, headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])
        code = r.json()['entity'][0]['code']
        print code
        content1 = {'userId':usrId, 'parentCode': code}
        r = requests.get(url=self.url, params=content1, headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])
        code = r.json()['entity'][0]['code']
        content1 = {'userId': usrId, 'parentCode': code}
        r = requests.get(url=self.url, params=content1, headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_02_parentCodeNull(self):
        '''parentCoded为空'''
        usr = get_IdOrToken('15652002619')
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId':usrId}
        r = requests.get(url=self.url, params=content, headers=usrheader,timeout=2)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"parentCode不能为空  ")
        self.assertIsNone(r.json()['entity'])

    def test_03_userIdNull(self):
        '''userId为空'''
        usr = get_IdOrToken('15652002619')
        usrId = usr[0]
        usrheader = usr[2]
        content = {'parentCode':0}
        r = requests.get(url=self.url, params=content, headers=usrheader,timeout=2)
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请求参数不正确")
        self.assertIsNone(r.json()['entity'])

    def test_04_AllNull(self):
        '''userId,区域编码都为空'''
        usr = get_IdOrToken('15652002619')
        usrId = usr[0]
        usrheader = usr[2]
        r = requests.get(url=self.url, headers=usrheader,timeout=2)
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请求参数不正确")
        self.assertIsNone(r.json()['entity'])

    def tearDown(self):
        print u"#################自动执行测试结束##############"

if __name__ == '__main__':
    unittest.main()


