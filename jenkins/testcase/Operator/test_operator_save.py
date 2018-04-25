#coding=utf-8
import sys,unittest,requests,random,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
class Save(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url = 'http://10.10.100.163:8085/ucenter/operator/save'
        self.a=random.randint(1,1000000)

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''用户第一次提交服务商信息,信用代码为18位，企业名称为20位，法人为10位汉字'''
        # usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usr = get_IdOrToken('13700000008')
        usrId = usr[0]
        usrheader = usr[2]
        content={             # 运营商id
                 'userId':usrId,#用户id
                 'licenseName':u'我是一个二十位数字的汉字你懂吗不懂你可以',# 公司全名称
                 'licenseNo':123456789012345681,  #社会统一信用代码
                 'licenseLegalName':u'我是一个十位的数字啊',#法人
                 'licenceImg':1,#营业执照
                 'licenseBegTime':1,#营业执照有效期开始时间
                 'licenseEndTime':1,#营业执照有效期截止时间
                 'licenseType':1,#营业执照类型
                 'licenseAddress':1,#营业执照住所
                 'licenseWealth':1, #营业执照注册资本
                 'licenseStartTime':1,#营业执照成立日期
                 'operatorsAccountId':1,#运营商账户
                 'companyBankCard':'1234567890',#公司对公账号
                 'companyBankName':1,#对公账号开户行
                 'conpanyPhone':1,#公司座机
                 'companyLegal':1,#法人
                 'companyName':1,#企业名称
                 'areaCode':1,#区域编码
                 'status':1,#状态
                 'money':1,#服务费，押金
                 'createTime':1,#创建时间
                 'reason':1,#审核意见
                 'operatorsImg':1,#运营商二维码
                 'areaName':1  #区域名称
                 }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''服务商提交信用代码为19位'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]

        content = {  # 运营商id
            'userId': usrId,  # 用户id
            'licenseName': u'一',  # 公司全名称
            'licenseNo': 1234567890123456789,  # 社会统一信用代码
            'licenseLegalName': u'两位',  # 法人
            'licenceImg': 1,  # 营业执照
            'licenseBegTime': 1,  # 营业执照有效期开始时间
            'licenseEndTime': 1,  # 营业执照有效期截止时间
            'licenseType': 1,  # 营业执照类型
            'licenseAddress': 1,  # 营业执照住所
            'licenseWealth': 1,  # 营业执照注册资本
            'licenseStartTime': 1,  # 营业执照成立日期
            'operatorsAccountId': 1,  # 运营商账户
            'companyBankCard': '12345678910',  # 公司对公账号
            'companyBankName': 1,  # 对公账号开户行
            'conpanyPhone': 1,  # 公司座机
            'companyLegal': 1,  # 法人
            'companyName': 1,  # 企业名称
            'areaCode': 1,  # 区域编码
            'status': 1,  # 状态
            'money': 1,  # 服务费，押金
            'createTime': 1,  # 创建时间
            'reason': 1,  # 审核意见
            'operatorsImg': 1,  # 运营商二维码
            'areaName': 1  # 区域名称
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'社会统一信用代码最小18位')


    def test_03_allTrue(self):
        '''服务商提交信用代码为17位'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]

        content = {  # 运营商id
            'userId': usrId,  # 用户id
            'licenseName': u'一二三四',  # 公司全名称
            'licenseNo': 12345678901234567,  # 社会统一信用代码
            'licenseLegalName': u'两位',  # 法人
            'licenceImg': 1,  # 营业执照
            'licenseBegTime': 1,  # 营业执照有效期开始时间
            'licenseEndTime': 1,  # 营业执照有效期截止时间
            'licenseType': 1,  # 营业执照类型
            'licenseAddress': 1,  # 营业执照住所
            'licenseWealth': 1,  # 营业执照注册资本
            'licenseStartTime': 1,  # 营业执照成立日期
            'operatorsAccountId': 1,  # 运营商账户
            'companyBankCard': 1234567890,  # 公司对公账号
            'companyBankName': 1,  # 对公账号开户行
            'conpanyPhone': 1,  # 公司座机
            'companyLegal': 1,  # 法人
            'companyName': 1,  # 企业名称
            'areaCode': 1,  # 区域编码
            'status': 1,  # 状态
            'money': 1,  # 服务费，押金
            'createTime': 1,  # 创建时间
            'reason': 1,  # 审核意见
            'operatorsImg': 1,  # 运营商二维码
            'areaName': 1  # 区域名称
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'社会统一信用代码最小18位')


    def test_04_allTrue(self):
        '''服务商提交信用代码为空'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]

        content = {  # 运营商id
            'userId': usrId,  # 用户id
            'licenseName': u'一二三',  # 公司全名称
            # 'licenseNo': 12345678901234567,  # 社会统一信用代码
            'licenseLegalName': u'两位',  # 法人
            'licenceImg': 1,  # 营业执照
            'licenseBegTime': 1,  # 营业执照有效期开始时间
            'licenseEndTime': 1,  # 营业执照有效期截止时间
            'licenseType': 1,  # 营业执照类型
            'licenseAddress': 1,  # 营业执照住所
            'licenseWealth': 1,  # 营业执照注册资本
            'licenseStartTime': 1,  # 营业执照成立日期
            'operatorsAccountId': 1,  # 运营商账户
            'companyBankCard':'12345',  # 公司对公账号
            'companyBankName': 1,  # 对公账号开户行
            'conpanyPhone': 1,  # 公司座机
            'companyLegal': 1,  # 法人
            'companyName': 1,  # 企业名称
            'areaCode': 1,  # 区域编码
            'status': 1,  # 状态
            'money': 1,  # 服务费，押金
            'createTime': 1,  # 创建时间
            'reason': 1,  # 审核意见
            'operatorsImg': 1,  # 运营商二维码
            'areaName': 1  # 区域名称
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'社会统一信用代码不能为null')

    def test_05_allTrue(self):
        '''服务商提交信用代码为汉字英文'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]

        content = {  # 运营商id
            'userId': usrId,  # 用户id
            'licenseName': u'一二三四',  # 公司全名称
            'licenseNo': u'A朱1234567890123456',  # 社会统一信用代码
            'licenseLegalName': u'两位',  # 法人
            'licenceImg': 1,  # 营业执照
            'licenseBegTime': 1,  # 营业执照有效期开始时间
            'licenseEndTime': 1,  # 营业执照有效期截止时间
            'licenseType': 1,  # 营业执照类型
            'licenseAddress': 1,  # 营业执照住所
            'licenseWealth': 1,  # 营业执照注册资本
            'licenseStartTime': 1,  # 营业执照成立日期
            'operatorsAccountId': 1,  # 运营商账户
            'companyBankCard':'12345678910',  # 公司对公账号
            'companyBankName': 1,  # 对公账号开户行
            'conpanyPhone': 1,  # 公司座机
            'companyLegal': 1,  # 法人
            'companyName': 1,  # 企业名称
            'areaCode': 1,  # 区域编码
            'status': 1,  # 状态
            'money': 1,  # 服务费，押金
            'createTime': 1,  # 创建时间
            'reason': 1,  # 审核意见
            'operatorsImg': 1,  # 运营商二维码
            'areaName': 1  # 区域名称
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'社会统一信用代码输入格式错误')

    def test_06_allTrue(self):
        '''服务商提交信用代码为空格'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]

        content = {  # 运营商id
            'userId': usrId,  # 用户id
            'licenseName': u'一二三四',  # 公司全名称
            'licenseNo': u'                  ',  # 社会统一信用代码
            'licenseLegalName': u'两位',  # 法人
            'licenceImg': 1,  # 营业执照
            'licenseBegTime': 1,  # 营业执照有效期开始时间
            'licenseEndTime': 1,  # 营业执照有效期截止时间
            'licenseType': 1,  # 营业执照类型
            'licenseAddress': 1,  # 营业执照住所
            'licenseWealth': 1,  # 营业执照注册资本
            'licenseStartTime': 1,  # 营业执照成立日期
            'operatorsAccountId': 1,  # 运营商账户
            'companyBankCard':'12345678910',  # 公司对公账号
            'companyBankName': 1,  # 对公账号开户行
            'conpanyPhone': 1,  # 公司座机
            'companyLegal': 1,  # 法人
            'companyName': 1,  # 企业名称
            'areaCode': 1,  # 区域编码
            'status': 1,  # 状态
            'money': 1,  # 服务费，押金
            'createTime': 1,  # 创建时间
            'reason': 1,  # 审核意见
            'operatorsImg': 1,  # 运营商二维码
            'areaName': 1  # 区域名称
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'社会统一信用代码输入格式错误')


    def test_07_allTrue(self):
        '''名称为21位'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]

        content = {  # 运营商id
            'userId': usrId,  # 用户id
            'licenseName': u'012345678901234567891',  # 公司全名称
            'licenseNo': 123456789012345687,  # 社会统一信用代码
            'licenseLegalName': u'两位',  # 法人
            'licenceImg': 1,  # 营业执照
            'licenseBegTime': 1,  # 营业执照有效期开始时间
            'licenseEndTime': 1,  # 营业执照有效期截止时间
            'licenseType': 1,  # 营业执照类型
            'licenseAddress': 1,  # 营业执照住所
            'licenseWealth': 1,  # 营业执照注册资本
            'licenseStartTime': 1,  # 营业执照成立日期
            'operatorsAccountId': 1,  # 运营商账户
            'companyBankCard': 1234567890,  # 公司对公账号
            'companyBankName': 1,  # 对公账号开户行
            'conpanyPhone': 1,  # 公司座机
            'companyLegal': 1,  # 法人
            'companyName': 1,  # 企业名称
            'areaCode': 1,  # 区域编码
            'status': 1,  # 状态
            'money': 1,  # 服务费，押金
            'createTime': 1,  # 创建时间
            'reason': 1,  # 审核意见
            'operatorsImg': 1,  # 运营商二维码
            'areaName': 1  # 区域名称
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'公司名称字数限制1-20位汉字')

    def test_08_allTrue(self):
        '''名称为3位'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]

        content = {  # 运营商id
            'userId': usrId,  # 用户id
            'licenseName': u'我是一',  # 公司全名称
            'licenseNo': 123456789012345687,  # 社会统一信用代码
            'licenseLegalName': u'两位',  # 法人
            'licenceImg': 1,  # 营业执照
            'licenseBegTime': 1,  # 营业执照有效期开始时间
            'licenseEndTime': 1,  # 营业执照有效期截止时间
            'licenseType': 1,  # 营业执照类型
            'licenseAddress': 1,  # 营业执照住所
            'licenseWealth': 1,  # 营业执照注册资本
            'licenseStartTime': 1,  # 营业执照成立日期
            'operatorsAccountId': 1,  # 运营商账户
            'companyBankCard': 1234567890,  # 公司对公账号
            'companyBankName': 1,  # 对公账号开户行
            'conpanyPhone': 1,  # 公司座机
            'companyLegal': 1,  # 法人
            'companyName': 1,  # 企业名称
            'areaCode': 1,  # 区域编码
            'status': 1,  # 状态
            'money': 1,  # 服务费，押金
            'createTime': 1,  # 创建时间
            'reason': 1,  # 审核意见
            'operatorsImg': 1,  # 运营商二维码
            'areaName': 1  # 区域名称
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'公司名称字数限制4-40位汉字')

    def test_09_allTrue(self):
        '''名称为空'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]

        content = {  # 运营商id
            'userId': usrId,  # 用户id
            # 'licenseName': u'我是一1',  # 公司全名称
            'licenseNo': 123456789012345687,  # 社会统一信用代码
            'licenseLegalName': u'两位',  # 法人
            'licenceImg': 1,  # 营业执照
            'licenseBegTime': 1,  # 营业执照有效期开始时间
            'licenseEndTime': 1,  # 营业执照有效期截止时间
            'licenseType': 1,  # 营业执照类型
            'licenseAddress': 1,  # 营业执照住所
            'licenseWealth': 1,  # 营业执照注册资本
            'licenseStartTime': 1,  # 营业执照成立日期
            'operatorsAccountId': 1,  # 运营商账户
            'companyBankCard': 1234567890,  # 公司对公账号
            'companyBankName': 1,  # 对公账号开户行
            'conpanyPhone': 1,  # 公司座机
            'companyLegal': 1,  # 法人
            'companyName': 1,  # 企业名称
            'areaCode': 1,  # 区域编码
            'status': 1,  # 状态
            'money': 1,  # 服务费，押金
            'createTime': 1,  # 创建时间
            'reason': 1,  # 审核意见
            'operatorsImg': 1,  # 运营商二维码
            'areaName': 1  # 区域名称
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'公司名称不能为null')

    def test_10_allTrue(self):
        '''名称为空格'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]

        content = {  # 运营商id
            'userId': usrId,  # 用户id
            'licenseName': u'          ',  # 公司全名称
            'licenseNo':123456789012345687,  # 社会统一信用代码
            'licenseLegalName': u'两位',  # 法人
            'licenceImg': 1,  # 营业执照
            'licenseBegTime': 1,  # 营业执照有效期开始时间
            'licenseEndTime': 1,  # 营业执照有效期截止时间
            'licenseType': 1,  # 营业执照类型
            'licenseAddress': 1,  # 营业执照住所
            'licenseWealth': 1,  # 营业执照注册资本
            'licenseStartTime': 1,  # 营业执照成立日期
            'operatorsAccountId': 1,  # 运营商账户
            'companyBankCard':1234567890,  # 公司对公账号
            'companyBankName': 1,  # 对公账号开户行
            'conpanyPhone': 1,  # 公司座机
            'companyLegal': 1,  # 法人
            'companyName': 1,  # 企业名称
            'areaCode': 1,  # 区域编码
            'status': 1,  # 状态
            'money': 1,  # 服务费，押金
            'createTime': 1,  # 创建时间
            'reason': 1,  # 审核意见
            'operatorsImg': 1,  # 运营商二维码
            'areaName': 1  # 区域名称
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'公司名称不能为null')

    def test_11_allTrue(self):
            '''法人名字为11位'''
            usr = get_IdOrToken(sql(allSql()['sql6'])[0])
            usrId = usr[0]
            usrheader = usr[2]
            content = {  # 运营商id
                'userId': usrId,  # 用户id
                'licenseName': u'我是一个二十位数字的汉字你懂吗不懂你可以',  # 公司全名称
                'licenseNo': 123456789012345678,  # 社会统一信用代码
                'licenseLegalName': u'我是一个十位的汉字啊的',  # 法人
                'licenceImg': 1,  # 营业执照
                'licenseBegTime': 1,  # 营业执照有效期开始时间
                'licenseEndTime': 1,  # 营业执照有效期截止时间
                'licenseType': 1,  # 营业执照类型
                'licenseAddress': 1,  # 营业执照住所
                'licenseWealth': 1,  # 营业执照注册资本
                'licenseStartTime': 1,  # 营业执照成立日期
                'operatorsAccountId': 1,  # 运营商账户
                'companyBankCard':1234567890,  # 公司对公账号
                'companyBankName': 1,  # 对公账号开户行
                'conpanyPhone': 1,  # 公司座机
                'companyLegal': 1,  # 法人
                'companyName': 1,  # 企业名称
                'areaCode': 1,  # 区域编码
                'status': 1,  # 状态
                'money': 1,  # 服务费，押金
                'createTime': 1,  # 创建时间
                'reason': 1,  # 审核意见
                'operatorsImg': 1,  # 运营商二维码
                'areaName': 1  # 区域名称
            }
            r = requests.post(url=self.url, data=content, headers=usrheader)
            print r.content
            print r.json()
            self.assertEqual(r.status_code, 403)
            self.assertEqual(r.json()['code'], 2000)
            self.assertEqual(r.json()['success'], False)
            self.assertEqual(r.json()['message'], u'法人信息10位')

    def test_12_allTrue(self):
        '''法人名字为1位'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]
        content = {  # 运营商id
                    'userId': usrId,  # 用户id
                    'licenseName': u'我是一个二十位数字的汉字你懂吗不懂你可以',  # 公司全名称
                    'licenseNo': 123456789012345687,  # 社会统一信用代码
                    'licenseLegalName': u'我',  # 法人
                    'licenceImg': 1,  # 营业执照
                    'licenseBegTime': 1,  # 营业执照有效期开始时间
                    'licenseEndTime': 1,  # 营业执照有效期截止时间
                    'licenseType': 1,  # 营业执照类型
                    'licenseAddress': 1,  # 营业执照住所
                    'licenseWealth': 1,  # 营业执照注册资本
                    'licenseStartTime': 1,  # 营业执照成立日期
                    'operatorsAccountId': 1,  # 运营商账户
                    'companyBankCard': 1234567890123456,  # 公司对公账号
                    'companyBankName': 1,  # 对公账号开户行
                    'conpanyPhone': 1,  # 公司座机
                    'companyLegal': 1,  # 法人
                    'companyName': 1,  # 企业名称
                    'areaCode': 1,  # 区域编码
                    'status': 1,  # 状态
                    'money': 1,  # 服务费，押金
                    'createTime': 1,  # 创建时间
                    'reason': 1,  # 审核意见
                    'operatorsImg': 1,  # 运营商二维码
                    'areaName': 1  # 区域名称
                }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'法人信息10位')

    def test_13_allTrue(self):
        '''法人名字为特殊字符'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]
        content = {  # 运营商id
                    'userId': usrId,  # 用户id
                    'licenseName': u'我是一个二十位数字的汉字你懂吗不懂你可以',  # 公司全名称
                    'licenseNo': 123456789012345687,  # 社会统一信用代码
                    'licenseLegalName': u'我~*&……',  # 法人
                    'licenceImg': 1,  # 营业执照
                    'licenseBegTime': 1,  # 营业执照有效期开始时间
                    'licenseEndTime': 1,  # 营业执照有效期截止时间
                    'licenseType': 1,  # 营业执照类型
                    'licenseAddress': 1,  # 营业执照住所
                    'licenseWealth': 1,  # 营业执照注册资本
                    'licenseStartTime': 1,  # 营业执照成立日期
                    'operatorsAccountId': 1,  # 运营商账户
                    'companyBankCard': 1234567890,  # 公司对公账号
                    'companyBankName': 1,  # 对公账号开户行
                    'conpanyPhone': 1,  # 公司座机
                    'companyLegal': 1,  # 法人
                    'companyName': 1,  # 企业名称
                    'areaCode': 1,  # 区域编码
                    'status': 1,  # 状态
                    'money': 1,  # 服务费，押金
                    'createTime': 1,  # 创建时间
                    'reason': 1,  # 审核意见
                    'operatorsImg': 1,  # 运营商二维码
                    'areaName': 1  # 区域名称
                }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'法人信息只能输入中英文')

    def test_14_allTrue(self):
        '''法人名字为空'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]
        content = {  # 运营商id
                    'userId': usrId,  # 用户id
                    'licenseName': u'我是一个二十位数字的汉字你懂吗不懂你可以',  # 公司全名称
                    'licenseNo': 123456789012345687,  # 社会统一信用代码
                    # 'licenseLegalName': u'我~*&……',  # 法人
                    'licenceImg': 1,  # 营业执照
                    'licenseBegTime': 1,  # 营业执照有效期开始时间
                    'licenseEndTime': 1,  # 营业执照有效期截止时间
                    'licenseType': 1,  # 营业执照类型
                    'licenseAddress': 1,  # 营业执照住所
                    'licenseWealth': 1,  # 营业执照注册资本
                    'licenseStartTime': 1,  # 营业执照成立日期
                    'operatorsAccountId': 1,  # 运营商账户
                    'companyBankCard': 1234567890123456,  # 公司对公账号
                    'companyBankName': 1,  # 对公账号开户行
                    'conpanyPhone': 1,  # 公司座机
                    'companyLegal': 1,  # 法人
                    'companyName': 1,  # 企业名称
                    'areaCode': 1,  # 区域编码
                    'status': 1,  # 状态
                    'money': 1,  # 服务费，押金
                    'createTime': 1,  # 创建时间
                    'reason': 1,  # 审核意见
                    'operatorsImg': 1,  # 运营商二维码
                    'areaName': 1  # 区域名称
                }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'法人不能为null')

    def test_15_allTrue(self):
        '''新用户重复提交已认证的统一信用代码'''
        usr = get_IdOrToken(18600000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {  # 运营商id
                   'userId': usrId,  # 用户id
                   'licenseName': u'一二三四',  # 公司全名称
                   'licenseNo': 123456789012345678,  # 社会统一信用代码
                   'licenseLegalName': u'两位',  # 法人
                   'licenceImg': 1,  # 营业执照
                   'licenseBegTime': 1,  # 营业执照有效期开始时间
                   'licenseEndTime': 1,  # 营业执照有效期截止时间
                   'licenseType': 1,  # 营业执照类型
                   'licenseAddress': 1,  # 营业执照住所
                   'licenseWealth': 1,  # 营业执照注册资本
                   'licenseStartTime': 1,  # 营业执照成立日期
                   'operatorsAccountId': 1,  # 运营商账户
                   'companyBankCard': 1234567890,  # 公司对公账号
                   'companyBankName': 1,  # 对公账号开户行
                   'conpanyPhone': 1,  # 公司座机
                   'companyLegal': 1,  # 法人
                   'companyName': 1,  # 企业名称
                   'areaCode': 1,  # 区域编码
                   'status': 1,  # 状态
                   'money': 1,  # 服务费，押金
                   'createTime': 1,  # 创建时间
                   'reason': 1,  # 审核意见
                   'operatorsImg': 1,  # 运营商二维码
                   'areaName': 1  # 区域名称
                   }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 17003)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u'该企业已被认证，请重新填写')

    def test_16_allTrue(self):
        '''开户银行51个字符'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]
        content={             # 运营商id
                 'userId':usrId,#用户id
                 'licenseName':u'我是一个二十位数字的汉字你懂吗不懂你可以',# 公司全名称
                 'licenseNo':123456789012345681,  #社会统一信用代码
                 'licenseLegalName':u'我是一个十位的数字啊',#法人
                 'licenceImg':1,#营业执照
                 'licenseBegTime':1,#营业执照有效期开始时间
                 'licenseEndTime':1,#营业执照有效期截止时间
                 'licenseType':1,#营业执照类型
                 'licenseAddress':1,#营业执照住所
                 'licenseWealth':1, #营业执照注册资本
                 'licenseStartTime':1,#营业执照成立日期
                 'operatorsAccountId':1,#运营商账户
                 'companyBankCard':1234567890,#公司对公账号
                 'companyBankName':123456789012345678901234567890123456789012345678901,#对公账号开户行
                 'conpanyPhone':1,#公司座机
                 'companyLegal':1,#法人
                 'companyName':1,#企业名称
                 'areaCode':1,#区域编码
                 'status':1,#状态
                 'money':1,#服务费，押金
                 'createTime':1,#创建时间
                 'reason':1,#审核意见
                 'operatorsImg':1,#运营商二维码
                 'areaName':1  #区域名称
                 }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'对公账号开户行字数限制在50个字符以内')

    def test_17_allTrue(self):
        '''开户银行为空'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]
        content={             # 运营商id
                 'userId':usrId,#用户id
                 'licenseName':u'我是一个二十位数字的汉字你懂吗不懂你可以',# 公司全名称
                 'licenseNo':123456789012345681,  #社会统一信用代码
                 'licenseLegalName':u'我是一个十位的数字啊',#法人
                 'licenceImg':1,#营业执照
                 'licenseBegTime':1,#营业执照有效期开始时间
                 'licenseEndTime':1,#营业执照有效期截止时间
                 'licenseType':1,#营业执照类型
                 'licenseAddress':1,#营业执照住所
                 'licenseWealth':1, #营业执照注册资本
                 'licenseStartTime':1,#营业执照成立日期
                 'operatorsAccountId':1,#运营商账户
                 'companyBankCard':1234567890,#公司对公账号
                 # 'companyBankName':123456789012345678901234567890123456789012345678901,#对公账号开户行
                 'conpanyPhone':1,#公司座机
                 'companyLegal':1,#法人
                 'companyName':1,#企业名称
                 'areaCode':1,#区域编码
                 'status':1,#状态
                 'money':1,#服务费，押金
                 'createTime':1,#创建时间
                 'reason':1,#审核意见
                 'operatorsImg':1,#运营商二维码
                 'areaName':1  #区域名称
                 }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'开户行不能为null')

    def test_18_allTrue(self):
        '''开户银行为空格'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]
        content={             # 运营商id
                 'userId':usrId,#用户id
                 'licenseName':u'我是一个二十位数字的汉字你懂吗不懂你可以',# 公司全名称
                 'licenseNo':123456789012345681,  #社会统一信用代码
                 'licenseLegalName':u'我是一个十位的数字啊',#法人
                 'licenceImg':1,#营业执照
                 'licenseBegTime':1,#营业执照有效期开始时间
                 'licenseEndTime':1,#营业执照有效期截止时间
                 'licenseType':1,#营业执照类型
                 'licenseAddress':1,#营业执照住所
                 'licenseWealth':1, #营业执照注册资本
                 'licenseStartTime':1,#营业执照成立日期
                 'operatorsAccountId':1234567890,#运营商账户
                 'companyBankCard':1234567890,#公司对公账号
                 'companyBankName':'        ',#对公账号开户行
                 'conpanyPhone':1,#公司座机
                 'companyLegal':1,#法人
                 'companyName':1,#企业名称
                 'areaCode':1,#区域编码
                 'status':1,#状态
                 'money':1,#服务费，押金
                 'createTime':1,#创建时间
                 'reason':1,#审核意见
                 'operatorsImg':1,#运营商二维码
                 'areaName':1  #区域名称
                 }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'开户行不能为null')

    def test_19_allTrue(self):
        '''开户账号大于20位'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]
        content={             # 运营商id
                 'userId':usrId,#用户id
                 'licenseName':u'我是一个二十位数字的汉字你懂吗不懂你可以',# 公司全名称
                 'licenseNo':123456789012345681,  #社会统一信用代码
                 'licenseLegalName':u'我是一个十位的数字啊',#法人
                 'licenceImg':1,#营业执照
                 'licenseBegTime':1,#营业执照有效期开始时间
                 'licenseEndTime':1,#营业执照有效期截止时间
                 'licenseType':1,#营业执照类型
                 'licenseAddress':1,#营业执照住所
                 'licenseWealth':1, #营业执照注册资本
                 'licenseStartTime':1,#营业执照成立日期
                 'operatorsAccountId':1,#运营商账户
                 'companyBankCard':123456789012345678901,#公司对公账号
                 'companyBankName':12345678901234567890123456789012345678,#对公账号开户行
                 'conpanyPhone':1,#公司座机
                 'companyLegal':1,#法人
                 'companyName':1,#企业名称
                 'areaCode':1,#区域编码
                 'status':1,#状态
                 'money':1,#服务费，押金
                 'createTime':1,#创建时间
                 'reason':1,#审核意见
                 'operatorsImg':1,#运营商二维码
                 'areaName':1  #区域名称
                 }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'对公账号限制20个字符以内')

    def test_20_allTrue(self):
        '''开户账号为9位'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]
        content={             # 运营商id
                 'userId':usrId,#用户id
                 'licenseName':u'我是一个二十位数字的汉字你懂吗不懂你可以',# 公司全名称
                 'licenseNo':123456789012345681,  #社会统一信用代码
                 'licenseLegalName':u'我是一个十位的数字啊',#法人
                 'licenceImg':1,#营业执照
                 'licenseBegTime':1,#营业执照有效期开始时间
                 'licenseEndTime':1,#营业执照有效期截止时间
                 'licenseType':1,#营业执照类型
                 'licenseAddress':1,#营业执照住所
                 'licenseWealth':1, #营业执照注册资本
                 'licenseStartTime':1,#营业执照成立日期
                 'operatorsAccountId':1,#运营商账户
                 'companyBankCard':123456789,#公司对公账号
                 'companyBankName':12345678901234567890123456789012345678,#对公账号开户行
                 'conpanyPhone':1,#公司座机
                 'companyLegal':1,#法人
                 'companyName':1,#企业名称
                 'areaCode':1,#区域编码
                 'status':1,#状态
                 'money':1,#服务费，押金
                 'createTime':1,#创建时间
                 'reason':1,#审核意见
                 'operatorsImg':1,#运营商二维码
                 'areaName':1  #区域名称
                 }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'对公账号限制20个字符以内')

    def test_21_allTrue(self):
        '''开户账号为字母汉字特殊字符'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]
        content={             # 运营商id
                 'userId':usrId,#用户id
                 'licenseName':u'我是一个二十位数字的汉字你懂吗不懂你可以',# 公司全名称
                 'licenseNo':123456789012345681,  #社会统一信用代码
                 'licenseLegalName':u'我是一个十位的数字啊',#法人
                 'licenceImg':1,#营业执照
                 'licenseBegTime':1,#营业执照有效期开始时间
                 'licenseEndTime':1,#营业执照有效期截止时间
                 'licenseType':1,#营业执照类型
                 'licenseAddress':1,#营业执照住所
                 'licenseWealth':1, #营业执照注册资本
                 'licenseStartTime':1,#营业执照成立日期
                 'operatorsAccountId':1,#运营商账户
                 'companyBankCard':u'我你uuu#￥',#公司对公账号
                 'companyBankName':12345678901234567890123456789012345678,#对公账号开户行
                 'conpanyPhone':1,#公司座机
                 'companyLegal':1,#法人
                 'companyName':1,#企业名称
                 'areaCode':1,#区域编码
                 'status':1,#状态
                 'money':1,#服务费，押金
                 'createTime':1,#创建时间
                 'reason':1,#审核意见
                 'operatorsImg':1,#运营商二维码
                 'areaName':1  #区域名称
                 }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'对公账户数据类型错误')

    def test_22_allTrue(self):
        '''开户账号为空'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]
        content={             # 运营商id
                 'userId':usrId,#用户id
                 'licenseName':u'我是一个二十位数字的汉字你懂吗不懂你可以',# 公司全名称
                 'licenseNo':123456789012345681,  #社会统一信用代码
                 'licenseLegalName':u'我是一个十位的数字啊',#法人
                 'licenceImg':1,#营业执照
                 'licenseBegTime':1,#营业执照有效期开始时间
                 'licenseEndTime':1,#营业执照有效期截止时间
                 'licenseType':1,#营业执照类型
                 'licenseAddress':1,#营业执照住所
                 'licenseWealth':1, #营业执照注册资本
                 'licenseStartTime':1,#营业执照成立日期
                 'operatorsAccountId':1,#运营商账户
                 # 'companyBankCard':u'我你uuu#￥',#公司对公账号
                 'companyBankName':12345678901234567890123456789012345678,#对公账号开户行
                 'conpanyPhone':1,#公司座机
                 'companyLegal':1,#法人
                 'companyName':1,#企业名称
                 'areaCode':1,#区域编码
                 'status':1,#状态
                 'money':1,#服务费，押金
                 'createTime':1,#创建时间
                 'reason':1,#审核意见
                 'operatorsImg':1,#运营商二维码
                 'areaName':1  #区域名称
                 }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'公司对公账号不能为空')

    def test_23_allTrue(self):
        '''开户账号为空格'''
        usr = get_IdOrToken(sql(allSql()['sql6'])[0])
        usrId = usr[0]
        usrheader = usr[2]
        content={             # 运营商id
                 'userId':usrId,#用户id
                 'licenseName':u'我是一个二十位数字的汉字你懂吗不懂你可以',# 公司全名称
                 'licenseNo':123456789012345681,  #社会统一信用代码
                 'licenseLegalName':u'我是一个十位的数字啊',#法人
                 'licenceImg':1,#营业执照
                 'licenseBegTime':1,#营业执照有效期开始时间
                 'licenseEndTime':1,#营业执照有效期截止时间
                 'licenseType':1,#营业执照类型
                 'licenseAddress':1,#营业执照住所
                 'licenseWealth':1, #营业执照注册资本
                 'licenseStartTime':1,#营业执照成立日期
                 'operatorsAccountId':1,#运营商账户
                 'companyBankCard':u'      ',#公司对公账号
                 'companyBankName':12345678901234567890123456789012345678,#对公账号开户行
                 'conpanyPhone':1,#公司座机
                 'companyLegal':1,#法人
                 'companyName':1,#企业名称
                 'areaCode':1,#区域编码
                 'status':1,#状态
                 'money':1,#服务费，押金
                 'createTime':1,#创建时间
                 'reason':1,#审核意见
                 'operatorsImg':1,#运营商二维码
                 'areaName':1  #区域名称
                 }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,403)
        self.assertEqual(r.json()['code'],2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'],u'公司对公账号不能为空')

if __name__ == '__main__':
    unittest.main()
