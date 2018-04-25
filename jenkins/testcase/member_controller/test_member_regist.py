#coding=utf-8
import sys,unittest,requests,random,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *

class member_registerdUser(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url1 = 'http://10.10.100.206/ucenter/member/sendRegisterMessage'
        self.url2= 'http://10.10.100.206/ucenter/member/checkVerificationCode'
        self.url = 'http://10.10.100.206/ucenter/member/registeredUser'
        self.noregistum=int(C(sql(allSql()['sql1'])))

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_all_true(self):
        ''' 输入正确的手机号11位，密码6位，token'''
        mobile = {'mobile': self.noregistum}
        # mobile = {'mobile':18600000001}
        print mobile['mobile']
        r = requests.post(url=self.url1, data=mobile)
        print r.json()
       # 连接到数据库
        conn = MySQLdb.connect(host='10.10.100.206', port=3306, user='root', passwd='admin', db='smedia_center',charset='utf8')
        cur = conn.cursor()
        cur.execute('select text from s_sms_log where tel=%s order by appdate desc limit 1'%mobile['mobile'])
        data = cur.fetchall()
        vitycode = data[0][0][3:9]
        # print vitycode
        cur.close()
        content={'userName':mobile['mobile'],'code':vitycode}
        # print content['userName']
        r = requests.get(url=self.url2,params=content)
        print r.content
        token = r.json()['entity']
        print r.json()['entity']
        headers = {'Content-Type': 'application/json'}
        content = 'userName=%s&userPwd=123456&token=%s'%(mobile['mobile'],token)
        r = requests.post(self.url+ "?" + content, headers=headers)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNone(r.json()['entity'])

    def test_02_errortoken(self):
        ''' 手机号正常，密码正常，token为错误'''
        headers = {'Content-Type': 'application/json'}
        token='1234567890123456789012345678901234567890123'
        content = 'userName=18600000016&userPwd=123456&token=' + token
        r = requests.post(self.url + "?" + content, headers=headers)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],13001)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u'TOKEN验证失败')
        self.assertIsNone(r.json()['entity'])

    def test_03_Nonetoken(self):
        ''' 手机号正常，密码正常，token为空'''
        headers = {'Content-Type': 'application/json'}
        content = 'userName=18600000016&userPwd=123456'
        r = requests.post(self.url + "?" + content, headers=headers)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'token不能为空')
        self.assertIsNone(r.json()['entity'])

    def test_04_42token(self):
        '''手机号正常，密码正常，token为42位'''
        headers = {'Content-Type': 'application/json'}
        token = '123456789012345678901234567890123456789012'
        content = 'userName=18600000016&userPwd=123456&token=' + token
        r = requests.post(self.url + "?" + content, headers=headers)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 13001)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'],u'TOKEN验证失败')
        self.assertIsNone(r.json()['entity'])

    def test_05_44token(self):
        '''手机号正常，密码正常，token为44位'''
        headers = {'Content-Type': 'application/json'}
        token = '12345678901234567890123456789012345678901231'
        content = 'userName=18600000016&userPwd=123456&token=' + token
        r = requests.post(self.url + "?" + content, headers=headers)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 13001)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'],u'TOKEN验证失败')
        self.assertIsNone(r.json()['entity'])

    def test_06_0phonenum(self):
        '''0位的手机号'''
        headers = {'Content-Type': 'application/json'}
        token = '1234567890123456789012345678901234567890123'
        content ='userPwd=123456&token=' + token
        r = requests.post(self.url + "?" + content, headers=headers)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'],u'用户名手机号不能为空')
        self.assertIsNone(r.json()['entity'])

    def test_07_more11num(self):
        ''' 大于11位的手机号'''
        headers = {'Content-Type': 'application/json'}
        token = '1234567890123456789012345678901234567890123'
        content = 'userName=186000000161&userPwd=123456&token=' + token
        r = requests.post(self.url + "?" + content, headers=headers)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertIn(r.json()['message'],u'手机格式错误手机号长度11位')
        self.assertIsNone(r.json()['entity'])

    def test_08_8num(self):
        '''8位的手机号'''
        headers = {'Content-Type': 'application/json'}
        token = '1234567890123456789012345678901234567890123'
        content = 'userName=18600000&userPwd=123456&token=' + token
        r = requests.post(self.url + "?" + content, headers=headers)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertIn(r.json()['message'],u'手机格式错误手机号长度11位')
        self.assertIsNone(r.json()['entity'])

    def test_09_phoneparmas(self):
        ''' 手机号为字符串'''
        headers = {'Content-Type': 'application/json'}
        token = '1234567890123456789012345678901234567890123'
        content = 'userName='+'￥$'+'&userPwd=123456&token='+ token
        r = requests.post(self.url + "?" + content, headers=headers)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertIn(r.json()['message'],u'手机格式错误手机号长度11位')
        self.assertIsNone(r.json()['entity'])

    def test_10_11combine(self):
        '''手机号为字母数字组合11位'''
        headers = {'Content-Type': 'application/json'}
        token = '1234567890123456789012345678901234567890123'
        content = 'userName='+'~！652002619'+'&userPwd=123456&token=' + token
        r = requests.post(self.url + "?" + content, headers=headers)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'],u'手机格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_11_firstnum(self):
        '''手机号首字母不为1'''
        headers = {'Content-Type': 'application/json'}
        token = '1234567890123456789012345678901234567890123'
        content = 'userName=28600000016&userPwd=123456&token=' + token
        r = requests.post(self.url + "?" + content, headers=headers)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'],u'手机格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_12_11blank(self):
        '''手机号为空格11位'''
        headers = {'Content-Type': 'application/json'}
        token = '1234567890123456789012345678901234567890123'
        content = 'userPwd=123456&token=' + token
        r = requests.post(self.url + "?" + content, headers=headers)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'用户名手机号不能为空')
        self.assertIsNone(r.json()['entity'])

    def test_14_passwdChina(self):
        ''' 密码为设置为中文'''
        mobile = {'mobile': self.noregistum}
        print mobile['mobile']
        r = requests.post(url=self.url1, data=mobile)
        print r.json()
        # 连接到数据库
        conn = MySQLdb.connect(host='10.10.100.206', port=3306, user='root', passwd='admin', db='smedia_center',
                               charset='utf8')
        cur = conn.cursor()
        cur.execute('select text from s_sms_log order by appdate desc limit 1')
        data = cur.fetchall()
        vitycode = data[0][0][3:9]
        # print vitycode
        cur.close()
        content = {'userName': mobile['mobile'], 'code': vitycode}
        # print content['userName']
        r = requests.get(url=self.url2, params=content)
        # print r.json()
        token = r.json()['entity']
        print r.json()['entity']
        headers = {'Content-Type': 'application/json'}
        content = 'userName=%s&userPwd=%s&token=%s'%(mobile['mobile'],u'朱海豹123！！',token)
        r = requests.post(self.url + "?" + content, headers=headers)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'密码格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_15_passwd20(self):
        '''手机密码为20位'''
        mobile = {'mobile': self.noregistum}
        print mobile['mobile']
        r = requests.post(url=self.url1, data=mobile)
        print r.json()
        # 连接到数据库
        conn = MySQLdb.connect(host='10.10.100.206', port=3306, user='root', passwd='admin', db='smedia_center',
                               charset='utf8')
        cur = conn.cursor()
        cur.execute('select text from s_sms_log where tel=%s order by appdate desc limit 1'%mobile['mobile'])
        data = cur.fetchall()
        vitycode = data[0][0][3:9]
        # print vitycode
        cur.close()
        content = {'userName': mobile['mobile'], 'code': vitycode}
        # print content['userName']
        r = requests.get(url=self.url2, params=content)
        # print r.json()
        token = r.json()['entity']
        print r.json()['entity']
        headers = {'Content-Type': 'application/json'}
        content = 'userName=' + str(mobile['mobile']) + '&userPwd='+'12345678901234567890'+'&token=' + token
        r = requests.post(self.url + "?" + content, headers=headers)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNone(r.json()['entity'])

    def test_16_passwd21(self):
        '''手机密码为21位'''
        mobile = {'mobile': self.noregistum}
        print mobile['mobile']
        r = requests.post(url=self.url1, data=mobile)
        print r.json()
        # 连接到数据库
        conn = MySQLdb.connect(host='10.10.100.206', port=3306, user='root', passwd='admin', db='smedia_center',
                               charset='utf8')
        cur = conn.cursor()
        cur.execute('select text from s_sms_log order by appdate desc limit 1')
        data = cur.fetchall()
        vitycode = data[0][0][3:9]
        # print vitycode
        cur.close()
        content = {'userName': mobile['mobile'], 'code': vitycode}
        # print content['userName']
        r = requests.get(url=self.url2, params=content)
        # print r.json()
        token = r.json()['entity']
        print r.json()['entity']
        headers = {'Content-Type': 'application/json'}
        content = 'userName=%s&userPwd=123456789012345678901&token=%s'%(mobile['mobile'],token)
        r = requests.post(self.url+ "?" + content, headers=headers)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'],False)
        self.assertIn(r.json()['message'], u"密码长度至少6位最多20位密码格式错误")
        self.assertIsNone(r.json()['entity'])

if __name__ == '__main__':
    unittest.main()


