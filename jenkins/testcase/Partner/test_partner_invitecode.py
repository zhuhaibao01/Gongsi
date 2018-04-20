#coding=utf-8
import sys,unittest,requests
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
class get_operators_invite(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url='http://10.10.100.206/ucenter/member/partner/invite/code'
        self.PartnerNotInvite= AutoMysqlPhoneIsOrNo('17600365340')
        self.PartnerInvite = AutoMysqlPhoneIsOrNo('13611346409')

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''获取的手机号没有邀请码'''
        usr = get_IdOrToken(self.PartnerInvite)
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

    def test_02_allTrue(self):
        '''获取的手机号包含邀请码'''
        usr = get_IdOrToken(self.PartnerInvite)
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


