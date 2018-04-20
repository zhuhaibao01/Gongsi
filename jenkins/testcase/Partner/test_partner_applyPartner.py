#coding=utf-8
import sys,unittest,requests
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
class idcard_idCardAuth(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url = 'http://10.10.100.206/ucenter/member/partner/applyPartner'
        self.phone1 = AutoMysqlPhoneIsOrNo('13700000088')
        self.IdcardPassphone = AutoMysqlPhoneIsOrNo('13800000025')

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''有邀请码的用户进行新媒人认证，只填usrId和邀请码'''
        usr = get_IdOrToken(self.IdcardPassphone)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId':usrId, 'beInviteCode':123457}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''没有邀请码的用户进行新媒人认证，只填usrId和申请人区域编码和服务商Id'''
        usr = get_IdOrToken(self.IdcardPassphone)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId, 'addressCode': 110000,'operatorId':0}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_03_allTrue(self):
        '''有邀请码的用户进行新媒人认证，只填usrId和邀请码,邀请码为5位数字'''
        usr = get_IdOrToken(self.IdcardPassphone)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId':usrId, 'beInviteCode':12345}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 7007)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"邀请码不存在，请填写正确的邀请码！")
        self.assertIsNone(r.json()['entity'])

    def test_04_allTrue(self):
        '''有邀请码的用户进行新媒人认证，只填usrId和邀请码,邀请码为12位数字'''
        usr = get_IdOrToken(self.IdcardPassphone)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId':usrId, 'beInviteCode':123456789012}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 7007)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"邀请码不存在，请填写正确的邀请码！")
        self.assertIsNone(r.json()['entity'])

    def test_05_allTrue(self):
        '''有邀请码的用户进行新媒人认证，只填usrId和邀请码,邀请码为6位空格'''
        usr = get_IdOrToken(self.IdcardPassphone)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId':usrId, 'beInviteCode':'      '}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 7007)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"邀请码不存在，请填写正确的邀请码！")
        self.assertIsNone(r.json()['entity'])

    def test_06_allTrue(self):
        '''有邀请码的用户进行新媒人认证，只填usrId和邀请码,邀请码为6位汉字'''
        usr = get_IdOrToken(self.IdcardPassphone)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId':usrId, 'beInviteCode':u'我是六位汉字'}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 7007)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"邀请码不存在，请填写正确的邀请码！")
        self.assertIsNone(r.json()['entity'])

    def test_07_userIdappled(self):
        '''申请的新媒人已认证'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId, 'addressCode': 120100,'operatorId':0}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 10004)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"新媒人信息已认证")
        self.assertIsNone(r.json()['entity'])


if __name__ == '__main__':
    unittest.main()


