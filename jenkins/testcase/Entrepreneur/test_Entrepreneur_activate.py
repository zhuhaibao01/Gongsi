#coding=utf-8
import sys,unittest,requests,random,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
from CreateChinese import *
class License(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url = 'http://10.10.100.206/ucenter/ent/activate'
        self.phone1=AutoMysqlPhoneIsOrNo('13700000001')
        self.phone2 = AutoMysqlPhoneIsOrNo('13700000002')
        self.phone3 = AutoMysqlPhoneIsOrNo('13700000003')
        self.phone6 = AutoMysqlPhoneIsOrNo('13700000006')

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''只完成身份验证进行激活'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],15010)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'企业信息不完善')
        self.assertIsNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''只完成营业执照进行激活'''
        usr = get_IdOrToken(self.phone2)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],15010)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'企业信息不完善')
        self.assertIsNone(r.json()['entity'])

    def test_03_allTrue(self):
        '''只完成企业对公账号进行激活'''
        usr = get_IdOrToken(self.phone3)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],15010)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'企业信息不完善')
        self.assertIsNone(r.json()['entity'])

    def test_04_allTrue(self):
        '''完成三项认证信息进行激活'''
        usr = get_IdOrToken(self.phone6)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_05_allTrue(self):
        '''对已经激活的企业主进行激活'''
        usr = get_IdOrToken(self.phone6)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
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