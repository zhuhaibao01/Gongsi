#coding=utf-8
import sys,unittest,requests,random,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
from CreateChinese import *
class SaveBankCard(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url = 'http://10.10.100.206/ucenter/ent/save/bankCard'
        self.phone5 = AutoMysqlPhoneIsOrNo('13700000003')
        self.phone6 = AutoMysqlPhoneIsOrNo('13700000006')

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''验证企业对公账号，开户银行为50个字符，对公账号19位数字内'''
        usr = get_IdOrToken(self.phone6)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'bankAccountNumber':1234567890123456,  # 公司银行账号
                   'accountOpeningBank': createChinese(50),  # 开户银行
                   'mobilePhoneNumber': 15652002619,  # 开户手机号码
                   'userId':usrId
                   }
        r = requests.post(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''验证户银行大于50个字符'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'bankAccountNumber':1234567890123456,  # 公司银行账号
                   'accountOpeningBank': createChinese(51),  # 开户银行
                   'mobilePhoneNumber': 15652002619,  # 开户手机号码
                   'userId':usrId
                   }
        r = requests.post(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'开户银行限制50个字符以内')
        self.assertIsNone(r.json()['entity'])
    #
    def test_03_allTrue(self):
        '''验证开户银行为空'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'bankAccountNumber':1234567890123456,  # 公司银行账号
                   # 'accountOpeningBank': createChinese(51),  # 开户银行
                   'mobilePhoneNumber': 15652002619,  # 开户手机号码
                   'userId':usrId
                   }
        r = requests.post(url=self.url, params=content,headers=usrheader)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'开户银行不能为空')
        self.assertIsNone(r.json()['entity'])
    #
    #
    def test_04_allTrue(self):
        '''验证开户银行为空格'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'bankAccountNumber': 1234567890123456,  # 公司银行账号
            'accountOpeningBank': '       ',  # 开户银行
            'mobilePhoneNumber': 15652002619,  # 开户手机号码
            'userId': usrId
        }
        r = requests.post(url=self.url, params=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'开户银行不能为空')
        self.assertIsNone(r.json()['entity'])
    #
    def test_05_allTrue(self):
        '''验证开户银行为特殊字符'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'bankAccountNumber': 1234567890123456,  # 公司银行账号
            'accountOpeningBank': '~！@#￥%……&*（）',  # 开户银行
            'mobilePhoneNumber': 15652002619,  # 开户手机号码
            'userId': usrId
        }
        r = requests.post(url=self.url, params=content, headers=usrheader)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNotNone(r.json()['entity'])
    #
    def test_06_allTrue(self):
        '''验证企业对公账号为21位数字'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'bankAccountNumber':123456789012345678901,  # 公司银行账号
                   'accountOpeningBank': createChinese(50),  # 开户银行
                   'mobilePhoneNumber': 15652002619,  # 开户手机号码
                   'userId':usrId
                   }
        r = requests.post(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'银行卡账号限制20个字符以内')
        self.assertIsNone(r.json()['entity'])

    def test_07_allTrue(self):
        '''验证企业对公账号为9位数字'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'bankAccountNumber': 123456789,  # 公司银行账号
            'accountOpeningBank': createChinese(50),  # 开户银行
            'mobilePhoneNumber': 15652002619,  # 开户手机号码
            'userId': usrId
        }
        r = requests.post(url=self.url, params=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'银行卡账号限制20个字符以内')
        self.assertIsNone(r.json()['entity'])

    def test_08_allTrue(self):
        '''验证企业对公账号为空'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   # 'bankAccountNumber':12345678901234567890,  # 公司银行账号
                   'accountOpeningBank': createChinese(50),  # 开户银行
                   'mobilePhoneNumber': 15652002619,  # 开户手机号码
                   'userId':usrId
                   }
        r = requests.post(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'公司银行账号不能为空')
        self.assertIsNone(r.json()['entity'])

    def test_09_allTrue(self):
        '''验证企业对公账号为汉字'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'bankAccountNumber':createChinese(19),  # 公司银行账号
                   'accountOpeningBank': createChinese(50),  # 开户银行
                   'mobilePhoneNumber': 15652002619,  # 开户手机号码
                   'userId':usrId
                   }
        r = requests.post(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'对公账户数据类型错误')
        self.assertIsNone(r.json()['entity'])

    def test_10_allTrue(self):
        '''验证企业对公账号为空格'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'bankAccountNumber':'            ',  # 公司银行账号
            'accountOpeningBank': createChinese(50),  # 开户银行
            'mobilePhoneNumber': 15652002619,  # 开户手机号码
            'userId': usrId
        }
        r = requests.post(url=self.url, params=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertIn(r.json()['message'], u'公司银行账号不能为空对公账户数据类型错误')
        self.assertIsNone(r.json()['entity'])

    def test_11_allTrue(self):
        '''验证企业对公账号为特殊字符'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'bankAccountNumber': '~！@#￥%……&*（）',  # 公司银行账号
            'accountOpeningBank': createChinese(50),  # 开户银行
            'mobilePhoneNumber': 15652002619,  # 开户手机号码
            'userId': usrId
        }
        r = requests.post(url=self.url, params=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'对公账户数据类型错误')
        self.assertIsNone(r.json()['entity'])

    def test_12_allTrue(self):
        '''手机号为11位汉字'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'bankAccountNumber':123456789012345678,  # 公司银行账号
                   'accountOpeningBank': createChinese(50),  # 开户银行
                   'mobilePhoneNumber': createChinese(11),  # 开户手机号码
                   'userId':usrId
                   }
        r = requests.post(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'手机格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_13_allTrue(self):
        '''手机号为空'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'bankAccountNumber':123456789012345678,  # 公司银行账号
                   'accountOpeningBank': createChinese(50),  # 开户银行
                   # 'mobilePhoneNumber': createChinese(11),  # 开户手机号码
                   'userId':usrId
                   }
        r = requests.post(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'开户手机号码不能为空')
        self.assertIsNone(r.json()['entity'])
    #
    def test_14_allTrue(self):
        '''手机号为空格'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'bankAccountNumber':12345678901234567,  # 公司银行账号
                   'accountOpeningBank': createChinese(50),  # 开户银行
                   'mobilePhoneNumber':'           ',  # 开户手机号码
                   'userId':usrId
                   }
        r = requests.post(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertIn(r.json()['message'],u'开户手机号码不能为空手机格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_15_allTrue(self):
        '''手机号为特殊字符'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'bankAccountNumber':123456789012345678,  # 公司银行账号
                   'accountOpeningBank': createChinese(50),  # 开户银行
                   'mobilePhoneNumber':'~！@#￥%……&*（）——',  # 开户手机号码
                   'userId':usrId
                   }
        r = requests.post(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'手机格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_16_allTrue(self):
        '''手机号为12位'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'bankAccountNumber':123456789012345678,  # 公司银行账号
                   'accountOpeningBank': createChinese(50),  # 开户银行
                   'mobilePhoneNumber':'15652002619',  # 开户手机号码
                   'userId':usrId
                   }
        r = requests.post(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_17_allTrue(self):
        '''手机号为10位'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'bankAccountNumber':123456789012345678,  # 公司银行账号
                   'accountOpeningBank': createChinese(20),  # 开户银行
                   'mobilePhoneNumber':'1565200261',  # 开户手机号码
                   'userId':usrId
                   }
        r = requests.post(url=self.url, params=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'手机格式错误')
        self.assertIsNone(r.json()['entity'])

if __name__ == '__main__':
    unittest.main()