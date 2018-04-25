#coding=utf-8
import sys,unittest,requests,random,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
class member_controller_sendRegistMessage(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url='http://10.10.100.206/ucenter/member/sendRegisterMessages'
        self.noregistum =int(C(sql(allSql()['sql1'])))

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_noregist(self):
        ''' 发送正确的未注册的11位手机号'''
        mobile = {'mobile': self.noregistum}
        print mobile['mobile']
        r = requests.post(url=self.url, data=mobile)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNone(r.json()['entity'])

    def test_02_exitregist(self):
        ''' 发送正确的已注册的11位手机号'''
        mobile={'mobile':sql(allSql()['sql1'])[random.randint(1,len(allSql()['sql1']))]}
        r = requests.post(url=self.url,data=mobile)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNone(r.json()['entity'])

    def test_03_oposition(self):
        ''' 发送手机号为空'''
        r = requests.post(url=self.url)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'手机号不能为空')
        self.assertIsNone(r.json()['entity'])

    def test_04_12position(self):
        ''' 发送手机号超过11位'''
        mobile={'mobile':186000000011}
        r = requests.post(url=self.url,data=mobile)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertIn(r.json()['message'],u'手机号长度11位手机格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_05_8position(self):
        ''' 发送手机号为8位'''
        mobile={'mobile':18600000}
        r = requests.post(url=self.url,data=mobile)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertIn(r.json()['message'],u'手机号长度11位手机格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_06_param(self):
        ''' 发送的手机号为字符串'''
        mobile={'mobile':'！@#￥%#￥*@！#'}
        r = requests.post(url=self.url,data=mobile)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'手机格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_07_numparam(self):
        ''' 发送手机号为字母数字组合11位'''
        mobile={'mobile':'1~!@ 8%+w$^'}
        r = requests.post(url=self.url,data=mobile)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u'手机格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_08_first(self):
        ''' 发送手机号首字母不为1'''
        mobile={'mobile':28600000001}
        r = requests.post(url=self.url,data=mobile)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u'手机格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_09_blank(self):
        ''' 发送手机号为空格11位'''
        r = requests.post(url=self.url)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u'手机号不能为空')
        self.assertIsNone(r.json()['entity'])

    @unittest.skip(u'time to long')
    def test_10_more(self):
        ''' 发送验证码超过10次'''
        mobile={'mobile':15652002619}
        r = requests.post(url=self.url,data=mobile)
        for i in range(1, 11):
            time.sleep(60)
            r=requests.post(url=self.url,data=mobile)
        r = requests.post(url=self.url, data=mobile)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],5003)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'当日发送验证码次数过多')
        self.assertIsNone(r.json()['entity'])

    def test_11_1minute(self):
        ''' 一分钟内发送验证码'''
        mobile = {'mobile': self.noregistum}
        print mobile['mobile']
        r = requests.post(url=self.url,data=mobile,timeout=5)
        r = requests.post(url=self.url, data=mobile)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],5005)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'1分钟内只能发送1条验证码')
        self.assertIsNone(r.json()['entity'])

    def test_12_phoneChina(self):
        ''' 手机号为汉字'''
        mobile={'mobile':u'朱海包!!!!!!!!!'}
        r = requests.post(url=self.url,data=mobile)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertIn(r.json()['message'], u'手机格式错误手机号长度11位')
        self.assertIsNone(r.json()['entity'])

if __name__ == '__main__':
    unittest.main()