#coding=utf-8
import unittest, sys, os, requests, json
sys.path.append('..')
sys.path.append(os.path.abspath(os.listdir('..')[0] + '/' +'../../'))
from Base.test_CreatePhoneNum import *
from Base.test_CreateChinese import *
class record(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url='http://10.10.100.206/ucenter/ent/save/license'
        self.phone1 = AutoMysqlPhoneIsOrNo('13700000001')
        self.phone2 = AutoMysqlPhoneIsOrNo('13700000002')
        self.phone3 = AutoMysqlPhoneIsOrNo('13700000003')
        self.phone6 = AutoMysqlPhoneIsOrNo('13700000006')
        self.phone51 = AutoMysqlPhoneIsOrNo('13700000051')
        self.phone54 = AutoMysqlPhoneIsOrNo('13700000054')

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''没有认证营业执照的账号保存营业执照选填项，统一信用码18位，名称40个汉字，法定代表人10个'''
        # usr = get_IdOrToken(self.phone6)
        usr = get_IdOrToken(self.phone54)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'licenceImg': 'AAA',  # 营业执照图片地址
                   'corpTax': 123456789012345678,  # 公司税号
                   'corpFname':createChinese(40),  # 公司全名称
                   # 'corpTax': 913101140938567200,  # 公司税号
                   # 'corpFname':u'麦腾国际贸易(上海)有限公司',  # 公司全名称
                   'bizValidityPeriod': 'CCC',  # 营业执照有效期
                   'legalRepresentative':createChinese(10),  # 营业执照上的法人信息
                   'foundingTime': u'2016年03月13日',  # 成立时间
                   # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
                   # 'registeredCapital': 'web',  # 注册资本
                   # 'registeredType': 1,  # 注册类型
                   'scope': createChinese(10), # 经营范围
                   'userId':usrId
                   }
        r = requests.post(url=self.url, data=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNotNone(r.json()['entity'])


    def test_02_allTrue(self):
        '''统一信用码19位'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': 1234567890123456789,  # 公司税号
            'corpFname': createChinese(40),  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative': createChinese(10),  # 营业执照上的法人信息
            'foundingTime': u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'统一社会信用代码最长18位')
        self.assertIsNone(r.json()['entity'])


    def test_03_allTrue(self):
        '''统一信用码17位'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': 1234567890123456,  # 公司税号
            'corpFname': createChinese(40),  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative': createChinese(10),  # 营业执照上的法人信息
            'foundingTime': u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'统一社会信用代码最长18位')
        self.assertIsNone(r.json()['entity'])

    def test_04_allTrue(self):
        '''统一信用码为空'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            # 'corpTax': 123456789012345678,  # 公司税号
            'corpFname': createChinese(40),  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative': createChinese(10),  # 营业执照上的法人信息
            'foundingTime': u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u'统一社会信用代码不为空')
        self.assertIsNone(r.json()['entity'])

    def test_05_allTrue(self):
        '''统一信用码为空格'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': '     ',  # 公司税号
            'corpFname': createChinese(40),  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative': createChinese(10),  # 营业执照上的法人信息
            'foundingTime':u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['success'],False)
        self.assertIn(r.json()['message'], u'统一社会信用代码不为空统一社会信用代码最长18位')
        self.assertIsNone(r.json()['entity'])


    def test_06_allTrue(self):
        '''统一信用码为特殊符号'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': '~!@#$%^&*()',  # 公司税号
            'corpFname': createChinese(40),  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative': createChinese(10),  # 营业执照上的法人信息
            'foundingTime': u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u'统一社会信用代码最长18位')
        self.assertIsNone(r.json()['entity'])

    def test_07_allTrue(self):
        '''企业名称为41个汉字'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': 123456789012345678,  # 公司税号
            'corpFname': createChinese(41),  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative': createChinese(10),  # 营业执照上的法人信息
            'foundingTime': u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'公司名称字符限制为40位')
        self.assertIsNone(r.json()['entity'])

    def test_08_allTrue(self):
        '''企业名称为3个汉字'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': 123456789012345678,  # 公司税号
            'corpFname': createChinese(3),  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative': createChinese(10),  # 营业执照上的法人信息
            'foundingTime': u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'公司名称字符限制为40位')
        self.assertIsNone(r.json()['entity'])

    def test_09_allTrue(self):
        '''企业名称为空'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': 123456789012345678,  # 公司税号
            # 'corpFname': createChinese(41),  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative': createChinese(10),  # 营业执照上的法人信息
            'foundingTime': u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'公司名称不能为空')
        self.assertIsNone(r.json()['entity'])

    def test_10_allTrue(self):
        '''企业名称包含特殊字符'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': 123456789012345678,  # 公司税号
            'corpFname':u'我中间~包含@特殊字符',  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative': createChinese(10),  # 营业执照上的法人信息
            'foundingTime': u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_11_allTrue(self):
        '''企业名称包含空格'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': 123456789012345678,  # 公司税号
            'corpFname': u'我中间       特殊字符',  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative': createChinese(10),  # 营业执照上的法人信息
            'foundingTime': u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_12_allTrue(self):
        '''法人代表为11个汉字'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': 123456789012345678,  # 公司税号
            'corpFname': createChinese(10),  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative': createChinese(11),  # 营业执照上的法人信息
            'foundingTime':u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'法人信息10位')
        self.assertIsNone(r.json()['entity'])

    def test_13_allTrue(self):
        '''法人代表为1个汉字'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': 123456789012345678,  # 公司税号
            'corpFname': createChinese(4),  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative': createChinese(1),  # 营业执照上的法人信息
            'foundingTime': u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'法人信息10位')
        self.assertIsNone(r.json()['entity'])

    def test_14_allTrue(self):
        '''法人代表为空'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': 123456789012345678,  # 公司税号
            'corpFname': createChinese(10),  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            # 'legalRepresentative': createChinese(11),  # 营业执照上的法人信息
            'foundingTime': u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'法人信息不能为空')
        self.assertIsNone(r.json()['entity'])

    def test_15_allTrue(self):
        '''法人代表为空格'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': 123456789012345678,  # 公司税号
            'corpFname': createChinese(10),  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative':'   ',  # 营业执照上的法人信息
            'foundingTime': u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'法人信息只能输入中英文')
        self.assertIsNone(r.json()['entity'])

    def test_16_allTrue(self):
        '''法人代表为特殊符号'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': 123456789012345678,  # 公司税号
            'corpFname': createChinese(10),  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative': '~！@#￥%……&*',  # 营业执照上的法人信息
            'foundingTime':u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'法人信息只能输入中英文')
        self.assertIsNone(r.json()['entity'])

    def test_17_allTrue(self):
        '''法人代表中间包含数字'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': 123456789012345678,  # 公司税号
            'corpFname': createChinese(10),  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative':u'张三123',  # 营业执照上的法人信息
            'foundingTime': u'2016年03月13日',  # 成立时间
            # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
            # 'registeredCapital': 'web',  # 注册资本
            # 'registeredType': 1,  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'法人信息只能输入中英文')
        self.assertIsNone(r.json()['entity'])

    def test_18_allTrue(self):
        '''认证营业执照的必填项+选填项'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': 123456789012345678,  # 公司税号
            'corpFname': createChinese(40),  # 公司全名称
            'bizValidityPeriod': '2018-1-3,2018-1-4',  # 营业执照有效期
            'legalRepresentative': createChinese(10),  # 营业执照上的法人信息
            'foundingTime':u'2016年03月13日',  # 成立时间
            'domicile': createChinese(10),  # 住所
            'registeredCapital': u'壹佰万',  # 注册资本
            'registeredType': u'有限责任公司',  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_19_allTrue(self):
        '''认证营业执照选填项的注册资本包含小写'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'licenceImg': 'AAA',  # 营业执照图片地址
            'corpTax': 123456789012345678,  # 公司税号
            'corpFname': createChinese(40),  # 公司全名称
            'bizValidityPeriod': 'CCC',  # 营业执照有效期
            'legalRepresentative': createChinese(10),  # 营业执照上的法人信息
            'foundingTime':u'2016年03月13日',  # 成立时间
            'domicile': createChinese(10),  # 住所
            'registeredCapital': u'壹佰万1千',  # 注册资本
            'registeredType': u'有限责任公司',  # 注册类型
            'scope': createChinese(10),  # 经营范围
            'userId': usrId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_21_allTrue(self):
        '''填写认证营业执照中成立时间格式不正确'''
        usr = get_IdOrToken(15652000003)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'licenceImg': 'AAA',  # 营业执照图片地址
                   'corpTax': 123456789012345679,  # 公司税号
                   'corpFname':u'测试企业',  # 公司全名称
                   'bizValidityPeriod': 'CCC',  # 营业执照有效期
                   'legalRepresentative':createChinese(10),  # 营业执照上的法人信息
                   'foundingTime': '2016-0313',  # 成立时间
                   # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
                   # 'registeredCapital': 'web',  # 注册资本
                   # 'registeredType': 1,  # 注册类型
                   'scope': createChinese(10), # 经营范围
                   'userId':usrId
                   }
        r = requests.post(url=self.url, data=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'成立日期格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_22_allTrue(self):
        '''普通首媒用户用已通过的营业执照账号'''
        # usr = get_IdOrToken(self.phone6)
        usr = get_IdOrToken(self.phone54)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'licenceImg': 'AAA',  # 营业执照图片地址
                   # 'corpTax': 123456789012345678,  # 公司税号
                   # 'corpFname':createChinese(40),  # 公司全名称
                   'corpTax': 913101140938567200,  # 公司税号
                   'corpFname':u'麦腾国际贸易(上海)有限公司',  # 公司全名称
                   'bizValidityPeriod': 'CCC',  # 营业执照有效期
                   'legalRepresentative':createChinese(10),  # 营业执照上的法人信息
                   'foundingTime': u'2016年03月13日',  # 成立时间
                   # 'domicile': u'河南省信阳市潢川县弋阳路办事处弋阳路4号',  # 住所
                   # 'registeredCapital': 'web',  # 注册资本
                   # 'registeredType': 1,  # 注册类型
                   'scope': createChinese(10), # 经营范围
                   'userId':usrId
                   }
        r = requests.post(url=self.url, data=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'企业主营业执照信息已存在')
        self.assertIsNone(r.json()['entity'])


if __name__ == '__main__':
    unittest.main()
