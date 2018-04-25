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
        self.url ='http://10.10.100.206/ucenter/ent/authentication/info'
        self.phone1 = AutoMysqlPhoneIsOrNo('13700000001')
        self.phone4 = AutoMysqlPhoneIsOrNo('13700000004')
        self.phone6 = AutoMysqlPhoneIsOrNo('13700000006')

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''未认证企业主认证信息获取'''
        usr = get_IdOrToken(self.phone4)
        # usr = get_IdOrToken('13700000005')
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],15001)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'当前用户不存在企业主信息，请认证企业主信息')
        self.assertIsNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''已认证未激活企业主认证信息获取'''
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
        self.assertIsNotNone(r.json()['entity'])

    def test_03_allTrue(self):
        '''提交激活待审核企业主认证信息获取'''
        usr = get_IdOrToken(self.phone6)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content,headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_04_allTrue(self):
        '''已激活待审核企业主认证信息获取'''
        usr = get_IdOrToken(sql(allSql()['sql7']))
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content,headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

if __name__ == '__main__':
    unittest.main()