#coding=utf-8
import sys,unittest,requests
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
class get_operators(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url='http://10.10.100.206/ucenter/member/partner/area/operators'
        self.phone3 = AutoMysqlPhoneIsOrNo('18600008881')
        self.passOperator = AutoMysqlPhoneIsOrNo('15652002619')
        self.xiaobai= AutoMysqlPhoneIsOrNo('13700000004')

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''areaCode下有成功认证服务商信息，userId跟 areaCode匹配'''
        usr = get_IdOrToken(self.passOperator)
        usrId = usr[0]
        usrheader = usr[2]
        content={'userId':usrId,'areaCode':120100}
        r=requests.get(url=self.url,params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''areaCode下有成功认证服务商信息，userId跟 areaCode不匹配'''
        usr = get_IdOrToken(self.passOperator)
        usrId = usr[0]
        usrheader = usr[2]
        content={'userId':usrId,'areaCode':120101}
        r=requests.get(url=self.url,params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_03_allTrue(self):
        '''areaCode没有认证服务商的信息，userId跟areaCode不匹配'''
        usr = get_IdOrToken(self.phone3)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId, 'areaCode': 120101}
        r = requests.get(url=self.url, params=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_04_allTrue(self):
        '''areaCode没有认证服务商的信息，userId跟areaCode匹配'''
        usr = get_IdOrToken(self.phone3)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId, 'areaCode': 1}
        r = requests.get(url=self.url, params=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_05_allTrue(self):
        '''获取空白用户已认证服务商的信息，'''
        usr = get_IdOrToken(self.xiaobai)
        usrId = usr[0]
        usrheader = usr[2]
        content={'userId':usrId}
        r=requests.get(url=self.url,params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

if __name__ == '__main__':
    unittest.main()


