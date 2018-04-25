#coding=utf-8
import sys,unittest,requests,random,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
class member_getInvitedCodeInfo(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url='http://10.10.100.206/ucenter/member/getInvitedCodeInfo'

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''新媒人认证，服务商认证'''
        usr = get_IdOrToken('13700000088')
        usrId = usr[0]
        usrheader = usr[2]
        content1 = {'userId':usrId,'type':'H'}
        r = requests.get(url=self.url, params=content1, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    @unittest.skipUnless(False,u'研发代码没有布置完整')
    def test_02_allTrue(self):
        '''服务商认证，tpye为Y,新媒人没有认证'''
        usr = get_IdOrToken('18888880301')
        usrId = usr[0]
        usrheader = usr[2]
        content1 = {'userId':usrId,'type':'Y'}
        r = requests.get(url=self.url, params=content1, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_03_allTrue(self):
        '''服务商认证，tpye为Y,新媒人认证'''
        usr = get_IdOrToken('15652002619')
        usrId = usr[0]
        usrheader = usr[2]
        content1 = {'userId':usrId,'type':'Y'}
        r = requests.get(url=self.url, params=content1, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

if __name__=='__main__':
    unittest.main()