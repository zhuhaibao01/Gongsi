#coding=utf-8
import sys,unittest,requests
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
class member_login(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url='http://10.10.100.206/ucenter/memberlogin/login'
        self.phone11= AutoMysqlPhoneIsOrNo('13700000011')
        self.phone10=AutoMysqlPhoneIsOrNo('13700000010')
        self.noregistum = int(C(sql(allSql()['sql1'])))
        self.Nullphone77 = AutoMysqlPhoneIsOrNo('13700000077')

    def test_01_exregist(self):
        '''新媒人邀请的普通用户，登录'''
        content={'userName':self.phone11,'userPwd':123456}
        r = requests.post(url=self.url,data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_02_exregist(self):
        '''已注册的手机号，没有新媒人和企业主认证信息'''
        content = {'userName': self.phone10, 'userPwd': 123456}
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_03_noregist(self):
        '''没有注册的手机号登录'''
        mobile = {'mobile': self.noregistum}
        print mobile['mobile']
        content={'userName':self.noregistum,'userPwd':123456}
        r = requests.post(url=self.url,data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],3013)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u"该用户还未注册")
        self.assertIsNone(r.json()['entity'])

    def test_04_0phoneposition(self):
        '''手机号为空,登录'''
        content={'userPwd':123456,}
        r = requests.post(url=self.url,data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u"手机号不能为空")
        self.assertIsNone(r.json()['entity'])

    def test_05_12phoneposition(self):
        '''大于11位的手机号登录'''
        content={'userName':186000000011,'userPwd':123456}
        r = requests.post(url=self.url,data=content)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertIn(r.json()['message'],u"手机格式错误手机号长度11位")
        self.assertIsNone(r.json()['entity'])

    def test_06_8position(self):
        '''8位的手机号登录'''
        content={'userName':15652002,'userPwd':123456}
        r = requests.post(url=self.url,data=content)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertIn(r.json()['message'],u"手机格式错误手机号长度11位")
        self.assertIsNone(r.json()['entity'])

    def test_07_phoneparams(self):
        '''手机号为字符串'''
        content={'userName':'~!@#$%~!@#$','userPwd':123456}
        r = requests.post(url=self.url,data=content)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u"手机格式错误")
        self.assertIsNone(r.json()['entity'])

    def test_08_numcombine(self):
        '''手机号为字母数字组合11位'''
        content={'userName':'~!1565200~!','userPwd':123456}
        r = requests.post(url=self.url,data=content)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u"手机格式错误")
        self.assertIsNone(r.json()['entity'])

    def test_09_firstnot1(self):
        '''手机号首字母不为1'''
        content={'userName':25652002100,'userPwd':123456}
        r = requests.post(url=self.url,data=content)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u"手机格式错误")
        self.assertIsNone(r.json()['entity'])

    def test_10_11blank(self):
        '''手机号为空格11位'''
        content={'userName':'           ','userPwd':123456}
        r = requests.post(url=self.url,data=content)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u"手机号不能为空")
        self.assertIsNone(r.json()['entity'])

    def test_11_pwdnone(self):
        '''登录密码为空'''
        content={'userName':18600000007}
        r = requests.post(url=self.url,data=content)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u"密码不能为空")
        self.assertIsNone(r.json()['entity'])

    def test_12_5passwd(self):
        '''密码为5位'''
        content={'userName':18600000002,'userPwd':'12345'}
        r = requests.post(url=self.url,data=content)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertIn(r.json()['message'],u"密码长度至少6位最多20位密码格式错误")
        self.assertIsNone(r.json()['entity'])

    def test_13_21passwd(self):
        '''密码为21位'''
        content={'userName':18600000003,'userPwd':'!1234567890!@#$%^&(!1'}
        r = requests.post(url=self.url,data=content)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertIn(r.json()['message'],u"密码长度至少6位最多20位密码格式错误")
        self.assertIsNone(r.json()['entity'])

    @unittest.skipUnless(False,u'登录密码错误跳过')
    def test_14_passwderror(self):
        '''登录密码错误时'''
        content={'userName':self.Nullphone77,'userPwd':654321}
        r = requests.post(url=self.url,data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],3014)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u"账号或者密码错误")
        self.assertIsNone(r.json()['entity'])

    def tearDown(self):
        print u"#################自动执行测试结束##############"
if __name__ == '__main__':
    unittest.main()