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
        self.url = 'http://10.10.100.207:8085/ucenter/ent/authentication/bankCard'
        self.phone3 = AutoMysqlPhoneIsOrNo('13700000003')
        self.phone4 = AutoMysqlPhoneIsOrNo('13700000004')
        self.phone5 = AutoMysqlPhoneIsOrNo('13700000005')

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''未填写企业主对公账号的用户'''
        usr = get_IdOrToken(self.phone5)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId':usrId}
        r = requests.get(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],15007)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'企业主对公账户信息未填写')
        self.assertIsNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''已填写企业主对公账号的用户'''
        usr = get_IdOrToken(self.phone3)
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
        '''填写普通账号的用户'''
        usr = get_IdOrToken(self.phone4)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId':usrId}
        r = requests.get(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],15001)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'当前用户不存在企业主信息，请认证企业主信息')
        self.assertIsNone(r.json()['entity'])

if __name__ == '__main__':
    unittest.main()