#coding=utf-8
import sys,unittest,requests,random,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
class pay_WxZhb(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url = 'http://10.10.100.206/ucenter/member/partner/applyPartner'
        usr = get_IdOrToken('13800000025')
        self.usrId = usr[0]
        self.usrheader = usr[2]
        content = {'userId':self.usrId, 'BeInviteCode': 123457}
        r = requests.post(url=self.url, data=content, headers=self.usrheader)
        self.bizCode = r.json()['entity']['bizCode']

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''id,支付类型为支付宝，账户编码，支付金额都正确'''
        url = 'http://10.10.100.206/ucenter/pingpp/get-pingxx-charge?' \
              'userId='+str(self.usrId)+ \
              '&channel=PINGPP_ALIPAY' + \
              '&bizCode='+self.bizCode+ \
              '&money=0.01'
        r = requests.post(url=url, headers=self.usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''id,支付类型为微信，账户编码，支付金额都正确'''
        url = 'http://10.10.100.206/ucenter/pingpp/get-pingxx-charge?' \
              'userId='+str(self.usrId)+ \
              '&channel=PINGPP_WX' +\
              '&bizCode='+self.bizCode+ \
              '&money=0.01'
        r = requests.post(url=url, headers=self.usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_03_IdNull(self):
        '''id为空'''
        url = 'http://10.10.100.207:8085/ucenter/pingpp/get-pingxx-charge?'+ \
              '&channel=PINGPP_WX' +\
              '&bizCode='+self.bizCode+ \
              '&money=0.01'
        r = requests.post(url=url, headers=self.usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请求参数不正确")
        self.assertIsNone(r.json()['entity'])

    def test_04_channerlNull(self):
        '''支付方式为空'''
        url = 'http://10.10.100.206/ucenter/pingpp/get-pingxx-charge?' \
              'userId='+str(self.usrId)+ \
              '&bizCode='+self.bizCode+ \
              '&money=0.01'
        r = requests.post(url=url, headers=self.usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"channel not null")
        self.assertIsNone(r.json()['entity'])

    def test_05_Otherchannerl(self):
        '''支付类型是除了支付宝微信的其他方式1'''
        url = 'http://10.10.100.206/ucenter/pingpp/get-pingxx-charge?' \
              'userId='+str(self.usrId)+ \
              '&channel=111' +\
              '&bizCode='+self.bizCode+ \
              '&money=0.01'
        r = requests.post(url=url, headers=self.usrheader)
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 501)
        self.assertEqual(r.json()['success'], False)
        self.assertIsNotNone(r.json()['message'])
        self.assertIsNone(r.json()['entity'])

    def test_06_bizCodeNull(self):
        '''账户编码为空'''
        url = 'http://10.10.100.206/ucenter/pingpp/get-pingxx-charge?' \
              'userId='+str(self.usrId)+ \
              '&channel=PINGPP_WX'+ \
              '&money=0.01'
        r = requests.post(url=url, headers=self.usrheader)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertIsNotNone(r.json()['message'])
        self.assertIsNone(r.json()['entity'])

    def test_07_bizCodeerror(self):
        '''账户编码错误'''
        url = 'http://10.10.100.206/ucenter/pingpp/get-pingxx-charge?'+ \
              'userId='+str(self.usrId)+ \
              '&channel=PINGPP_WX'+ \
              '&bizCode=1111'+ \
              '&money=0.01'
        r = requests.post(url=url, headers=self.usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 501)
        self.assertEqual(r.json()['success'], False)
        self.assertIsNotNone(r.json()['message'])
        self.assertIsNone(r.json()['entity'])

    def test_08_moneyNull(self):
        '''支付的金额为空'''
        url = 'http://10.10.100.206/ucenter/pingpp/get-pingxx-charge?' +\
              'userId='+str(self.usrId)+ \
              '&channel=PINGPP_WX' +\
              '&bizCode='+self.bizCode
        r = requests.post(url=url, headers=self.usrheader)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertIsNotNone(r.json()['message'])
        self.assertIsNone(r.json()['entity'])

    def test_09_money0(self):
        '''支付的金额为0'''
        url = 'http://10.10.100.206/ucenter/pingpp/get-pingxx-charge?'+ \
              'userId='+str(self.usrId)+ \
              '&channel=PINGPP_WX'+ \
              '&bizCode='+ self.bizCode+\
              '&money=0'
        r = requests.post(url=url, headers=self.usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 4012)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'账户系统异常')
        self.assertIsNone(r.json()['entity'])

    def test_10_moneymore(self):
        '''支付的金额为大于当前金额'''
        url = 'http://10.10.100.206/ucenter/pingpp/get-pingxx-charge?' \
              'userId='+str(self.usrId)+ \
              '&channel=PINGPP_WX' \
              '&bizCode='+ self.bizCode+\
              '&money=0.02'
        r = requests.post(url=url, headers=self.usrheader)
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

if __name__ == '__main__':
    unittest.main()


