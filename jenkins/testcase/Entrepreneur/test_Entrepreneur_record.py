#coding=utf-8
import sys,unittest,requests,random,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
from CreateChinese import *

class record(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        u"""
        法人名称 2-20位字符
        邀请码   6-11位数字
        公司名称 4-40位汉字
        """
        self.url = 'http://10.10.100.163:8085/ucenter/ent/record'
        # self.url = 'http://10.10.100.206/ucenter/ent/record'
        self.phone1 = AutoMysqlPhoneIsOrNo('13700000001')
        self.phone2 = AutoMysqlPhoneIsOrNo('13700000002')
        self.phone3 = AutoMysqlPhoneIsOrNo('13700000003')
        self.phone5 = AutoMysqlPhoneIsOrNo('13700000005')
        self.phone7 = AutoMysqlPhoneIsOrNo('13700000008')
        self.phone51 = AutoMysqlPhoneIsOrNo('13700000051')
        self.phone52 = AutoMysqlPhoneIsOrNo('13700000052')
        self.phone54 = AutoMysqlPhoneIsOrNo('13700000054')

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''没有邀请码的普通用户进行企业主认证,名字为40位'''
        # usr = get_IdOrToken(self.phone5)
        usr = get_IdOrToken(self.phone54)
        usrId = usr[0]
        print(usrId)
        usrheader = usr[2]
        content = {'companyName':createChinese(40),'userId':usrId}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''有邀请码的普通用户进行企业主认证,名称为40位'''
        usr = get_IdOrToken(self.phone52)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'companyName':createChinese(40),'userId':usrId,'invitationCode':'123457'}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_03_allTrue(self):
        '''没有邀请码的普通用户进行企业主认证,名字3位'''
        usr = get_IdOrToken(self.phone5)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'companyName':createChinese(3),'userId':usrId}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'公司名称输入长度错误')


    def test_04_allTrue(self):
        '''没有邀请码的普通用户进行企业主认证,名字为空'''
        usr = get_IdOrToken(self.phone5)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'userId': usrId}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'公司名称不能为空')


    def test_05_allTrue(self):
        '''没有邀请码的普通用户进行企业主认证,名字为空格'''
        usr = get_IdOrToken(self.phone5)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'companyName':'        ','userId': usrId}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'公司名称不能为空')

    def test_06_allTrue(self):
        '''没有邀请码的普通用户进行企业主认证,名字为特殊字符'''
        usr = get_IdOrToken(self.phone5)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'companyName': '~！@#￥%……&*（）', 'userId': usrId}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNotNone(r.json()['entity'])
    #
    def test_07_allTrue(self):
        '''没有邀请码的普通用户进行企业主认证,名字为包含数字和字母'''
        usr = get_IdOrToken(self.phone5)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'companyName': u'张三科技123ABC', 'userId': usrId}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_08_allTrue(self):
        '''有邀请码的普通用户进行企业主认证,邀请码为5位数字'''
        # usr = get_IdOrToken(self.phone7)
        usr = get_IdOrToken(self.phone5)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'companyName': createChinese(40), 'userId': usrId, 'invitationCode': '12345'}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'邀请码输入长度错误')

    def test_09_allTrue(self):
        '''有邀请码的普通用户进行企业主认证,邀请码为大于11位的数字'''
        usr = get_IdOrToken(self.phone7)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'companyName': createChinese(40), 'userId': usrId, 'invitationCode': '123456789012'}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'邀请码输入长度错误')

    def test_10_allTrue(self):
        '''有邀请码的普通用户进行企业主认证,邀请码为6位的汉字'''
        usr = get_IdOrToken(self.phone7)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'companyName': createChinese(40), 'userId': usrId, 'invitationCode': u'我是六位汉字'}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 7007)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'邀请码不存在，请填写正确的邀请码！')

    def test_11_allTrue(self):
        '''有邀请码的普通用户进行企业主认证,邀请码为6位的字母'''
        usr = get_IdOrToken(self.phone7)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'companyName': createChinese(40), 'userId': usrId, 'invitationCode': 'ABCdef'}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 7007)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'邀请码不存在，请填写正确的邀请码！')

    def test_12_allTrue(self):
        '''有邀请码的普通用户进行企业主认证,邀请码为特殊字符'''
        usr = get_IdOrToken(self.phone7)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'companyName': createChinese(40), 'userId': usrId, 'invitationCode': '~！@#￥%……&*'}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 7007)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'邀请码不存在，请填写正确的邀请码！')

    def test_13_allTrue(self):
        '''有邀请码的普通用户进行企业主认证,邀请码为空格'''
        usr = get_IdOrToken(self.phone7)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'companyName': createChinese(40), 'userId': usrId, 'invitationCode': '      '}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'], u'请求成功')

    def test_14_allTrue(self):
        '''普通用户输入已经认证激活的企业名称'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {'companyName':u'测试企业','userId':usrId,'invitationCode':123457}
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],3028)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'该企业已被认证请重新填写！')

if __name__ == '__main__':
    unittest.main()
