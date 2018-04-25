#coding=utf-8
import sys,unittest,requests,random
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *

class member_controller_checkmobile(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url='http://10.10.100.207:8085/ucenter/member/checkExistByMobile'
        self.noregistum = int(C(sql(allSql()['sql1'])))

    def test_01_phone_true(self):
        ''' 发送正确的未注册的11位手机号'''
        mobile = {'mobile': self.noregistum}
        print mobile['mobile']
        r = requests.get(url=self.url,params=mobile,timeout=5)
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u"请求成功")
        self.assertEqual(r.json()['entity'],0)

    def test_02_phone_exit(self):
        ''' 发送正确的已注册的11位手机号'''
        mobile={'mobile':sql(allSql()['sql1'])[random.randint(1,len(allSql()['sql1']))]}
        r = requests.get(url=self.url,params=mobile)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u"请求成功")
        self.assertEqual(r.json()['entity'],1)

    def test_03_phone_12position(self):
        ''' 输入12位的手机号'''
        mobile={'mobile':156520026191}
        r = requests.get(url=self.url,params=mobile)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertIn(r.json()['message'],u"手机格式错误手机号长度11位")
        self.assertIsNone(r.json()['entity'])

    def test_04_phone_0position(self):
        ''' 手机号为空'''
        r = requests.get(url=self.url)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u"手机号不能为空")
        self.assertIsNone(r.json()['entity'])

    def test_05_phone_8position(self):
        ''' 输入8位的手机号'''
        mobile={'mobile':15652002}
        r = requests.get(url=self.url,params=mobile)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertIn(r.json()['message'],u"手机号长度11位手机格式错误")
        self.assertIsNone(r.json()['entity'])

    def test_06_phone_params(self):
        ''' 输入字符串的手机号'''
        mobile = {'mobile':'~！@#￥%……&*（'}
        r = requests.get(url=self.url, params=mobile)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'],u"手机格式错误")
        self.assertIsNone(r.json()['entity'])

    def test_07_phone_paramscombine(self):
        ''' 手机号为字母数字组合11位'''
        mobile = {'mobile':'1565￥%……&*（'}
        r = requests.get(url=self.url, params=mobile)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'],u"手机格式错误")
        self.assertIsNone(r.json()['entity'])

    def test_08_phone_firstnumber(self):
        ''' 手机号首字母不为1'''
        mobile = {'mobile':'25652002619'}
        r = requests.get(url=self.url, params=mobile)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'],u"手机格式错误")
        self.assertIsNone(r.json()['entity'])

    def test_09_phone_11nonenumber(self):
        ''' 手机号为空格11位'''
        r = requests.get(url=self.url)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'],u"手机号不能为空")
        self.assertIsNone(r.json()['entity'])

    def test_10_phone_phoneChina(self):
        ''' 手机号为汉字'''
        mobile = {'mobile': u'朱海豹哦哦哦哦哦哦哦哦'}
        r = requests.get(url=self.url, params=mobile,timeout=1)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'],u"手机格式错误")
        self.assertIsNone(r.json()['entity'])

    def tearDown(self):
        print u"#################自动执行测试结束##############"

if __name__ == '__main__':
    unittest.main()