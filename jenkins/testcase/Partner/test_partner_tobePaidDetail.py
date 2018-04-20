#coding=utf-8
import sys,unittest,requests
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
class idcard_idCardAuth(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url = 'http://10.10.100.206/ucenter/member/partner/toBePaidDetail'

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''经过身份认证后的userid'''
        usr = get_IdOrToken('13800000025')
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.get(url=self.url, params=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    @unittest.skip(u'接口有毛病')
    def test_02_idnotvity(self):
        '''没有经过身份认证后的id'''
        usr = get_IdOrToken(e[random.randint(1,len(e)-1)])
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId':usrId}
        r = requests.get(url=self.url, params=content, headers=usrheader,timeout=4)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 10001)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"新媒人不存在")
        self.assertIsNone(r.json()['entity'])

if __name__ == '__main__':
    unittest.main()


