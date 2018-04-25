#coding=utf-8
import sys,unittest,requests,random,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
from CreateChinese import *

class Info(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url = 'http://10.10.100.206/ucenter/ent/info'
        self.phone1 = AutoMysqlPhoneIsOrNo('13700000001')
        self.phone2 = AutoMysqlPhoneIsOrNo('13700000002')
        self.phone3 = AutoMysqlPhoneIsOrNo('13700000003')
        self.phone4 = AutoMysqlPhoneIsOrNo('13700000004')
        self.phone5 = AutoMysqlPhoneIsOrNo('13700000005')
        self.phone6 = AutoMysqlPhoneIsOrNo('13700000006')
        self.phone51 = AutoMysqlPhoneIsOrNo('13700000051')

    def tearDown(self):
        print u"#################自动执行测试结束##############"


    def test_01_allTrue(self):
        '''获取未认证的企业主认证'''
        usr = get_IdOrToken(self.phone4)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content,headers=usrheader)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],15001)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'当前用户不存在企业主信息，请认证企业主信息')
        self.assertIsNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''获取已进行企业主认证待激活的企业主'''
        usr = get_IdOrToken(self.phone5)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content,headers=usrheader)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertEqual(r.json()['entity']['status'], 'NOT_ACTIVE')


    def test_03_allTrue(self):
        '''获取只进行身份认证的企业主的usrId'''
        usr = get_IdOrToken(self.phone1)
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
        self.assertEqual(r.json()['entity']['status'], 'NOT_ACTIVE')

    def test_04_allTrue(self):
        '''获取只进行营业执照认证的企业主的usrId'''
        usr = get_IdOrToken(self.phone51)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertEqual(r.json()['entity']['status'], 'NOT_ACTIVE')

    def test_05_allTrue(self):
        '''获取只进行企业对公账号的企业主的usrId'''
        usr = get_IdOrToken(self.phone3)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertEqual(r.json()['entity']['status'], 'NOT_ACTIVE')

    def test_06_allTrue(self):
        '''获取对身份认证，营业执照认证，对公账号认证成功但激活待审核的usrId'''
        usr = get_IdOrToken(self.phone6)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertEqual(r.json()['entity']['status'],'AUDIT')

    def test_07_allTrue(self):
        '''获取审核失败的企业主的usrId'''
        usr = get_IdOrToken('13954285906')
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertEqual(r.json()['entity']['status'], 'REJECT')

    def test_08_allTrue(self):
        '''获取已经认证企业主的usrId'''
        usr = get_IdOrToken('13919273370')
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
        self.assertEqual(r.json()['entity']['status'], 'ALREADY_ACTIVATED')

    def test_09_allTrue(self):
        '''获取已经认证企业主的usrId'''
        usr = get_IdOrToken('13919273370')
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
        self.assertEqual(r.json()['entity']['status'], 'ALREADY_ACTIVATED')

if __name__ == '__main__':
    unittest.main()