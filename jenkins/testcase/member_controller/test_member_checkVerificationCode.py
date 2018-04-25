#coding=utf-8
import sys,unittest,requests,random,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
class member_controller_checkVerificationCode(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.noregistum = int(C(sql(allSql()['sql1'])))
        self.url = 'http://10.10.100.206/ucenter/member/checkVerificationCode'

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_norigist(self):
        ''' 正确的未注册的11位手机号和正确的的验证码'''
        mobile = {'mobile': self.noregistum}
        print mobile['mobile']
        url = 'http://10.10.100.206/ucenter/member/sendRegisterMessage'
        r = requests.post(url=url, data=mobile)
        # 连接到数据库
        conn = MySQLdb.connect(host='10.10.100.206', port=3306, user='root', passwd='admin', db='smedia_center',charset='utf8')
        cur = conn.cursor()
        cur.execute('select text from s_sms_log order by appdate desc limit 1')
        data = cur.fetchall()
        vitycode = data[0][0][3:9]
        cur.close()
        content={'userName':mobile['mobile'],'code':vitycode}
        r = requests.get(url=self.url,params=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_02_exitregist(self):
        ''' 正确的未注册手机号，错误的验证码'''
        mobile = {'mobile':self.noregistum}
        print mobile['mobile']
        content = {'userName': mobile['mobile'], 'code':123456}
        r = requests.get(url=self.url, params=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],5001)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u"验证码有误")
        self.assertIsNone(r.json()['entity'])

    def test_03_0code(self):
        ''' 手机号正确、code为0位'''
        content={'userName':18600000014}
        r = requests.get(url=self.url,params=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u"验证码不能为空")
        self.assertIsNone(r.json()['entity'])

    def test_04_4code(self):
        ''' 手机号正确、code为4位'''
        content={'userName':18600000014,'code':1234}
        r = requests.get(url=self.url,params=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u"验证码6位")
        self.assertIsNone(r.json()['entity'])

    def test_05_5code(self):
        ''' 手机号正确、code为5位'''
        content={'userName':18600000014,'code':12345}
        r = requests.get(url=self.url,params=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u"验证码6位")
        self.assertIsNone(r.json()['entity'])

    def test_06_7code(self):
        ''' 手机号正确、code为7位'''
        content={'userName':18600000014,'code':1234567}
        r = requests.get(url=self.url,params=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u"验证码6位")
        self.assertIsNone(r.json()['entity'])

    def test_07_0phonenum(self):
        '''手机号为空、code正常'''
        content={'code':123456}
        r = requests.get(url=self.url,params=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u"用户名手机号不能为空")
        self.assertIsNone(r.json()['entity'])

    def test_08_11more(self):
        ''' 大于11位的手机号'''
        content={'userName':186000000141,'code':123456}
        r = requests.get(url=self.url,params=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertIn(r.json()['message'],u'手机号长度11位手机格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_09_7code(self):
        ''' 8位的手机号'''
        content={'userName':15652000,'code':123456}
        r = requests.get(url=self.url,params=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertIn(r.json()['message'],u"手机号长度11位手机格式错误")
        self.assertIsNone(r.json()['entity'])

    def test_10_phoneparam(self):
        ''' 手机号为字符串'''
        content={'userName':'~!@#~!^&* ^','code':123456}
        r = requests.get(url=self.url,params=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u"手机格式错误")
        self.assertIsNone(r.json()['entity'])

    def test_11_7code(self):
        '''手机号为字母数字组合11位'''
        self.url = 'http://10.10.100.207:8085/ucenter/member/checkVerificationCode'
        content={'userName':'!156!!~@#$#','code':123456}
        r = requests.get(url=self.url,params=content)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u"手机格式错误")
        self.assertIsNone(r.json()['entity'])

    def test_12_blank11(self):
        '''手机号为空格11位'''
        content={'userName':'           ','code':123456}
        r = requests.get(url=self.url,params=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertIn(r.json()['message'],u"手机格式错误用户名手机号不能为空")
        self.assertIsNone(r.json()['entity'])

if __name__ == '__main__':
    unittest.main()
