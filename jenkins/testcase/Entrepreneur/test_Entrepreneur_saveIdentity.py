#coding=utf-8
import sys,unittest,requests,random,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
from CreateChinese import *
class SaveIdentity(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        # self.url = 'http://10.10.100.163:8085/ucenter/ent/save/identity'
        self.url = 'http://10.10.100.206/ucenter/ent/save/identity'
        self.phone1 = AutoMysqlPhoneIsOrNo('13700000001')
        self.phone6 = AutoMysqlPhoneIsOrNo('13700000006')
        self.identyphone = AutoMysqlPhoneIsOrNo('15652000003')

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''只有法人进行身份认证,姓名为20个字符，公民身份证号18个数字，住址200个字符，签发机关100个字符'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'entrepreneurLegal.realName':createChinese(20),  # 真实姓名
                   'entrepreneurLegal.sex':u'男',  # 身份证性别
                   'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurLegal.birth': '1991-03-13',  # 出生
                   'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurLegal.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurLegal.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurLegal.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurLegal.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurLegal.issuingAgency':createChinese(40),  # 身份证签发机关
                   'userId':usrId    #userId
                   }
        r = requests.post(url=self.url, data=content,headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''姓名为21个字符'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                'entrepreneurLegal.realName': createChinese(20)+'1',  # 真实姓名
                'entrepreneurLegal.sex': u'男',  # 身份证性别
                'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                'entrepreneurLegal.birth': '1991-03-13',  # 出生
                'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
                'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
                'entrepreneurLegal.issuingAgency': createChinese(40),  # 身份证签发机关
                'userId': usrId  # userId
            }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'姓名至少2位，最大40位')
        self.assertIsNone(r.json()['entity'])

    def test_03_allTrue(self):
        '''姓名为1个字符'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                'entrepreneurLegal.realName': createChinese(1),  # 真实姓名
                'entrepreneurLegal.sex': u'男',  # 身份证性别
                'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                'entrepreneurLegal.birth': '1991-03-13',  # 出生
                'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
                'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
                'entrepreneurLegal.issuingAgency': createChinese(40),  # 身份证签发机关
                'userId': usrId  # userId
            }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'姓名至少2位，最大40位')
        self.assertIsNone(r.json()['entity'])

    def test_04_allTrue(self):
        '''姓名为空'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                # 'entrepreneurLegal.realName': createChinese(40) + '1',  # 真实姓名
                'entrepreneurLegal.sex': u'男',  # 身份证性别
                'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                'entrepreneurLegal.birth': '1991-03-13',  # 出生
                'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
                'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
                'entrepreneurLegal.issuingAgency': createChinese(40),  # 身份证签发机关
                'userId': usrId  # userId
            }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'真实姓名不能为空')
        self.assertIsNone(r.json()['entity'])
#
    def test_05_allTrue(self):
        '''姓名为空格'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'entrepreneurLegal.realName':'    ',  # 真实姓名
            'entrepreneurLegal.sex': u'男',  # 身份证性别
            'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurLegal.birth': '1991-03-13',  # 出生
            'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
            'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
            'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurLegal.issuingAgency': createChinese(40),  # 身份证签发机关
            'userId': usrId  # userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'真实姓名不能为空')
        self.assertIsNone(r.json()['entity'])
#
    def test_06_allTrue(self):
        '''姓名包含特殊字符'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'entrepreneurLegal.realName': '~！@#￥%……&*（）——+ ',  # 真实姓名
            'entrepreneurLegal.sex': u'男',  # 身份证性别
            'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurLegal.birth': '1991-03-13',  # 出生
            'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
            'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
            'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurLegal.issuingAgency': createChinese(40),  # 身份证签发机关
            'userId': usrId  # userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_07_allTrue(self):
        '''身份证号为19位'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
                'entrepreneurLegal.sex': u'男',  # 身份证性别
                'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                'entrepreneurLegal.birth': '1991-03-13',  # 出生
                'entrepreneurLegal.idNo': '4115261991031304910',  # 身份证号码
                'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
                'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
                'entrepreneurLegal.issuingAgency': createChinese(40),  # 身份证签发机关
                'userId': usrId  # userId
            }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'身份证格式错误')
        self.assertIsNone(r.json()['entity'])
#
    def test_08_allTrue(self):
        '''身份证号为17位'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
                'entrepreneurLegal.sex': u'男',  # 身份证性别
                'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                'entrepreneurLegal.birth': '1991-03-13',  # 出生
                'entrepreneurLegal.idNo': '41152619910313049',  # 身份证号码
                'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
                'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
                'entrepreneurLegal.issuingAgency': createChinese(40),  # 身份证签发机关
                'userId': usrId  # userId
            }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'身份证格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_09_allTrue(self):
        '''身份证号为空'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
                'entrepreneurLegal.sex': u'男',  # 身份证性别
                'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                'entrepreneurLegal.birth': '1991-03-13',  # 出生
                # 'entrepreneurLegal.idNo': '4115261991031304910',  # 身份证号码
                'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
                'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
                'entrepreneurLegal.issuingAgency': createChinese(40),  # 身份证签发机关
                'userId': usrId  # userId
            }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'身份证号码不能为空')
        self.assertIsNone(r.json()['entity'])

    def test_10_allTrue(self):
        '''身份证号为空格'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
            'entrepreneurLegal.sex': u'男',  # 身份证性别
            'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurLegal.birth': '1991-03-13',  # 出生
            'entrepreneurLegal.idNo': '                  ',  # 身份证号码
            'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
            'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurLegal.issuingAgency': createChinese(40),  # 身份证签发机关
            'userId': usrId  # userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertIn(r.json()['message'], u'法人身份证号码不能为空身份证格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_11_allTrue(self):
        '''身份证号包含特殊字符'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
            'entrepreneurLegal.sex': u'男',  # 身份证性别
            'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurLegal.birth': '1991-03-13',  # 出生
            'entrepreneurLegal.idNo': '~！@#￥%……&*（）——+ ',  # 身份证号码
            'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
            'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurLegal.issuingAgency': createChinese(40),  # 身份证签发机关
            'userId': usrId  # userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'身份证格式错误')
        self.assertIsNone(r.json()['entity'])
# #
    def test_12_allTrue(self):
        '''住址为201个字符'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
                'entrepreneurLegal.sex': u'男',  # 身份证性别
                'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                'entrepreneurLegal.birth': '1991-03-13',  # 出生
                'entrepreneurLegal.idNo': '411526199103130491',  # 身份证号码
                'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                'entrepreneurLegal.cardAddress': createChinese(201),  # 身份证的地址
                'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
                'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
                'entrepreneurLegal.issuingAgency': createChinese(40),  # 身份证签发机关
                'userId': usrId  # userId
            }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'地址限制为200个字符')
        self.assertIsNone(r.json()['entity'])

    def test_13_allTrue(self):
        '''住址为空'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
                'entrepreneurLegal.sex': u'男',  # 身份证性别
                'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                'entrepreneurLegal.birth': '1991-03-13',  # 出生
                'entrepreneurLegal.idNo': '411526199103130491',  # 身份证号码
                'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                'entrepreneurLegal.cardAddress': createChinese(201),  # 身份证的地址
                'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
                'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
                'entrepreneurLegal.issuingAgency': createChinese(40),  # 身份证签发机关
                'userId': usrId  # userId
            }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'地址限制为200个字符')
        self.assertIsNone(r.json()['entity'])

    def test_14_allTrue(self):
        '''住址为空格'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
            'entrepreneurLegal.sex': u'男',  # 身份证性别
            'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurLegal.birth': '1991-03-13',  # 出生
            'entrepreneurLegal.idNo': '4115261991031304910',  # 身份证号码
            'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurLegal.cardAddress':'       ',  # 身份证的地址
            'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurLegal.issuingAgency': createChinese(40),  # 身份证签发机关
            'userId': usrId  # userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertIn(r.json()['message'], u'法人身份证的地址不能为空身份证格式错误')
        self.assertIsNone(r.json()['entity'])
#
    def test_15_allTrue(self):
        '''住址为特殊字符'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
            'entrepreneurLegal.sex': u'男',  # 身份证性别
            'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurLegal.birth': '1991-03-13',  # 出生
            'entrepreneurLegal.idNo': '4115261991031304910',  # 身份证号码
            'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurLegal.cardAddress': '~！@#￥%……&*（）——+ ',  # 身份证的地址
            'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurLegal.issuingAgency': createChinese(40),  # 身份证签发机关
            'userId': usrId  # userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'身份证格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_16_allTrue(self):
        '''签发机关为101个字符'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
                'entrepreneurLegal.sex': u'男',  # 身份证性别
                'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                'entrepreneurLegal.birth': '1991-03-13',  # 出生
                'entrepreneurLegal.idNo': '411526199103130491',  # 身份证号码
                'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
                'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
                'entrepreneurLegal.issuingAgency': createChinese(101),  # 身份证签发机关
                'userId': usrId  # userId
            }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'签发机关限制为100个字符')
        self.assertIsNone(r.json()['entity'])

    def test_17_allTrue(self):
        '''签发机关为空'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
                'entrepreneurLegal.sex': u'男',  # 身份证性别
                'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                'entrepreneurLegal.birth': '1991-03-13',  # 出生
                'entrepreneurLegal.idNo': '411526199103130491',  # 身份证号码
                'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
                'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
                # 'entrepreneurLegal.issuingAgency': createChinese(101),  # 身份证签发机关
                'userId': usrId  # userId
            }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'身份证签发机关不能为空')
        self.assertIsNone(r.json()['entity'])
# #
    def test_18_allTrue(self):
        '''签发机关为空格'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
                'entrepreneurLegal.sex': u'男',  # 身份证性别
                'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                'entrepreneurLegal.birth': '1991-03-13',  # 出生
                'entrepreneurLegal.idNo': '411526199103130491',  # 身份证号码
                'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
                'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
                'entrepreneurLegal.issuingAgency':'     ',  # 身份证签发机关
                'userId': usrId  # userId
            }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'身份证签发机关不能为空')
        self.assertIsNone(r.json()['entity'])
#
    def test_19_allTrue(self):
        '''签发机关包含特殊字符'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
            'entrepreneurLegal.sex': u'男',  # 身份证性别
            'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurLegal.birth': '1991-03-13',  # 出生
            'entrepreneurLegal.idNo': '411526199103130491',  # 身份证号码
            'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
            'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurLegal.issuingAgency': '~！@#￥%……&*（）——+',  # 身份证签发机关
            'userId': usrId  # userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_20_allTrue(self):
        '''企业主申请当为代办人时,代办人姓名为20个字符，公民身份证号18个数字，住址200个字符，签发机关100个字符'''
        usr = get_IdOrToken(self.identyphone)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'entrepreneurAgency.realName':createChinese(20),  # 真实姓名
                   'entrepreneurAgency.sex': u'男',  # 身份证性别
                   'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
                   'entrepreneurAgency.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurAgency.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurAgency.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurAgency.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurAgency.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurAgency.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurAgency.issuingAgency':createChinese(100),  # 身份证签发机关
                   'entrepreneurAgency.proxyImg': 'AAA', # 委托协议
                   'entrepreneurLegal.realName':createChinese(20),  # 真实姓名
                   'entrepreneurLegal.sex':u'男',  # 身份证性别
                   'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurLegal.birth': '1991-03-13',  # 出生
                   'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurLegal.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurLegal.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurLegal.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurLegal.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurLegal.issuingAgency':createChinese(100),  # 身份证签发机关
                   'userId':usrId    #userId
                   }
        r = requests.post(url=self.url, data=content,headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'],u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_21_allTrue(self):
        '''代办人姓名为21个字符'''
        usr = get_IdOrToken(self.identyphone)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'entrepreneurAgency.realName':createChinese(20)+'1',  # 真实姓名
                   'entrepreneurAgency.sex': u'男',  # 身份证性别
                   'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
                   'entrepreneurAgency.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurAgency.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurAgency.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurAgency.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurAgency.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurAgency.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurAgency.issuingAgency':createChinese(100),  # 身份证签发机关
                   'entrepreneurAgency.proxyImg': 'AAA', # 委托协议
                   'entrepreneurLegal.realName':createChinese(20),  # 真实姓名
                   'entrepreneurLegal.sex':u'男',  # 身份证性别
                   'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurLegal.birth': '1991-03-13',  # 出生
                   'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurLegal.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurLegal.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurLegal.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurLegal.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurLegal.issuingAgency':createChinese(100),  # 身份证签发机关
                   'userId':usrId    #userId
            }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'姓名至少2位，最大40位')
        self.assertIsNone(r.json()['entity'])

    def test_22_allTrue(self):
        '''代办人姓名为1个字符'''
        usr = get_IdOrToken(self.identyphone)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'entrepreneurAgency.realName':'1',  # 真实姓名
                   'entrepreneurAgency.sex': u'男',  # 身份证性别
                   'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
                   'entrepreneurAgency.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurAgency.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurAgency.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurAgency.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurAgency.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurAgency.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurAgency.issuingAgency':createChinese(100),  # 身份证签发机关
                   'entrepreneurAgency.proxyImg': 'AAA', # 委托协议
                   'entrepreneurLegal.realName':createChinese(20),  # 真实姓名
                   'entrepreneurLegal.sex':u'男',  # 身份证性别
                   'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurLegal.birth': '1991-03-13',  # 出生
                   'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurLegal.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurLegal.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurLegal.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurLegal.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurLegal.issuingAgency':createChinese(100),  # 身份证签发机关
                   'userId':usrId    #userId
            }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'姓名至少2位，最大40位')
        self.assertIsNone(r.json()['entity'])

    def test_23_allTrue(self):
        '''代办人姓名为空'''
        usr = get_IdOrToken(self.identyphone)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            # 'entrepreneurAgency.realName': createChinese(20),  # 真实姓名
            'entrepreneurAgency.sex': u'男',  # 身份证性别
            'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
            'entrepreneurAgency.idNo': '41152619910313049X',  # 身份证号码
            'entrepreneurAgency.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurAgency.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurAgency.cardAddress': createChinese(200),  # 身份证的地址
            'entrepreneurAgency.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurAgency.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurAgency.issuingAgency': createChinese(100),  # 身份证签发机关
            'entrepreneurAgency.proxyImg': 'AAA',  # 委托协议
            'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
            'entrepreneurLegal.sex': u'男',  # 身份证性别
            'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurLegal.birth': '1991-03-13',  # 出生
            'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
            'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
            'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurLegal.issuingAgency': createChinese(100),  # 身份证签发机关
            'userId': usrId  # userId
            }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'真实姓名不能为空')
        self.assertIsNone(r.json()['entity'])


    def test_24_allTrue(self):
        '''代办人姓名为空格'''
        usr = get_IdOrToken(self.identyphone)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'entrepreneurAgency.realName':'  ',  # 真实姓名
            'entrepreneurAgency.sex': u'男',  # 身份证性别
            'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
            'entrepreneurAgency.idNo': '41152619910313049X',  # 身份证号码
            'entrepreneurAgency.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurAgency.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurAgency.cardAddress': createChinese(200),  # 身份证的地址
            'entrepreneurAgency.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurAgency.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurAgency.issuingAgency': createChinese(100),  # 身份证签发机关
            'entrepreneurAgency.proxyImg': 'AAA',  # 委托协议
            'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
            'entrepreneurLegal.sex': u'男',  # 身份证性别
            'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurLegal.birth': '1991-03-13',  # 出生
            'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
            'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
            'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurLegal.issuingAgency': createChinese(100),  # 身份证签发机关
            'userId': usrId  # userId
            }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'真实姓名不能为空')
        self.assertIsNone(r.json()['entity'])
# #
    def test_25_allTrue(self):
        '''代办人姓名为特殊字符'''
        usr = get_IdOrToken(self.identyphone)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'entrepreneurAgency.realName': '~！@#￥%……&*（）——+ ',  # 真实姓名
            'entrepreneurAgency.sex': u'男',  # 身份证性别
            'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
            'entrepreneurAgency.idNo': '41152619910313049X',  # 身份证号码
            'entrepreneurAgency.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurAgency.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurAgency.cardAddress': createChinese(200),  # 身份证的地址
            'entrepreneurAgency.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurAgency.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurAgency.issuingAgency': createChinese(100),  # 身份证签发机关
            'entrepreneurAgency.proxyImg': 'AAA',  # 委托协议
            'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
            'entrepreneurLegal.sex': u'男',  # 身份证性别
            'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurLegal.birth': '1991-03-13',  # 出生
            'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
            'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
            'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurLegal.issuingAgency': createChinese(100),  # 身份证签发机关
            'userId': usrId  # userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'],True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_26_allTrue(self):
        '''代办人身份证号为19位'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'entrepreneurAgency.realName':createChinese(20),  # 真实姓名
                   'entrepreneurAgency.sex': u'男',  # 身份证性别
                   'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
                   'entrepreneurAgency.idNo': '4115261991031304901',  # 身份证号码
                   'entrepreneurAgency.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurAgency.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurAgency.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurAgency.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurAgency.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurAgency.issuingAgency':createChinese(100),  # 身份证签发机关
                   'entrepreneurAgency.proxyImg': 'AAA', # 委托协议
                   'entrepreneurLegal.realName':createChinese(20),  # 真实姓名
                   'entrepreneurLegal.sex':u'男',  # 身份证性别
                   'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurLegal.birth': '1991-03-13',  # 出生
                   'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurLegal.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurLegal.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurLegal.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurLegal.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurLegal.issuingAgency':createChinese(100),  # 身份证签发机关
                   'userId':usrId    #userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'身份证格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_27_allTrue(self):
        '''代办人身份证号为空'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'entrepreneurAgency.realName':createChinese(20),  # 真实姓名
                   'entrepreneurAgency.sex': u'男',  # 身份证性别
                   'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
                   # 'entrepreneurAgency.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurAgency.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurAgency.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurAgency.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurAgency.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurAgency.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurAgency.issuingAgency':createChinese(100),  # 身份证签发机关
                   'entrepreneurAgency.proxyImg': 'AAA', # 委托协议
                   'entrepreneurLegal.realName':createChinese(20),  # 真实姓名
                   'entrepreneurLegal.sex':u'男',  # 身份证性别
                   'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurLegal.birth': '1991-03-13',  # 出生
                   'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurLegal.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurLegal.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurLegal.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurLegal.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurLegal.issuingAgency':createChinese(100),  # 身份证签发机关
                   'userId':usrId    #userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'身份证号码不能为空')
        self.assertIsNone(r.json()['entity'])

    def test_28_allTrue(self):
        '''代办人身份证号为空格'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'entrepreneurAgency.realName':createChinese(20),  # 真实姓名
                   'entrepreneurAgency.sex': u'男',  # 身份证性别
                   'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
                   'entrepreneurAgency.idNo': '                ',  # 身份证号码
                   'entrepreneurAgency.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurAgency.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurAgency.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurAgency.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurAgency.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurAgency.issuingAgency':createChinese(100),  # 身份证签发机关
                   'entrepreneurAgency.proxyImg': 'AAA', # 委托协议
                   'entrepreneurLegal.realName':createChinese(20),  # 真实姓名
                   'entrepreneurLegal.sex':u'男',  # 身份证性别
                   'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurLegal.birth': '1991-03-13',  # 出生
                   'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurLegal.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurLegal.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurLegal.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurLegal.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurLegal.issuingAgency':createChinese(100),  # 身份证签发机关
                   'userId':usrId    #userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertIn(r.json()['message'], u'代办人身份证号码不能为空身份证格式错误')
        self.assertIsNone(r.json()['entity'])
#
    def test_29_allTrue(self):
        '''代办人身份证号为特殊符号'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'entrepreneurAgency.realName': createChinese(20),  # 真实姓名
            'entrepreneurAgency.sex': u'男',  # 身份证性别
            'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
            'entrepreneurAgency.idNo': '~！@#￥%……&*（）————',  # 身份证号码
            'entrepreneurAgency.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurAgency.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurAgency.cardAddress': createChinese(200),  # 身份证的地址
            'entrepreneurAgency.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurAgency.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurAgency.issuingAgency': createChinese(100),  # 身份证签发机关
            'entrepreneurAgency.proxyImg': 'AAA',  # 委托协议
            'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
            'entrepreneurLegal.sex': u'男',  # 身份证性别
            'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurLegal.birth': '1991-03-13',  # 出生
            'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
            'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
            'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurLegal.issuingAgency': createChinese(100),  # 身份证签发机关
            'userId': usrId  # userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'身份证格式错误')
        self.assertIsNone(r.json()['entity'])

    def test_30_allTrue(self):
        '''代办人住址为201个字符'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'entrepreneurAgency.realName':createChinese(20),  # 真实姓名
                   'entrepreneurAgency.sex': u'男',  # 身份证性别
                   'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
                   'entrepreneurAgency.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurAgency.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurAgency.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurAgency.cardAddress': createChinese(201),  # 身份证的地址
                   'entrepreneurAgency.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurAgency.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurAgency.issuingAgency':createChinese(100),  # 身份证签发机关
                   'entrepreneurAgency.proxyImg': 'AAA', # 委托协议
                   'entrepreneurLegal.realName':createChinese(20),  # 真实姓名
                   'entrepreneurLegal.sex':u'男',  # 身份证性别
                   'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurLegal.birth': '1991-03-13',  # 出生
                   'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurLegal.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurLegal.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurLegal.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurLegal.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurLegal.issuingAgency':createChinese(100),  # 身份证签发机关
                   'userId':usrId    #userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'地址限制为200个字符')
        self.assertIsNone(r.json()['entity'])

    def test_31_allTrue(self):
        '''代办人住址为空'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'entrepreneurAgency.realName':createChinese(20),  # 真实姓名
                   'entrepreneurAgency.sex': u'男',  # 身份证性别
                   'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
                   'entrepreneurAgency.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurAgency.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurAgency.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurAgency.cardAddress': createChinese(201),  # 身份证的地址
                   'entrepreneurAgency.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurAgency.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurAgency.issuingAgency':createChinese(100),  # 身份证签发机关
                   'entrepreneurAgency.proxyImg': 'AAA', # 委托协议
                   'entrepreneurLegal.realName':createChinese(20),  # 真实姓名
                   'entrepreneurLegal.sex':u'男',  # 身份证性别
                   'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurLegal.birth': '1991-03-13',  # 出生
                   'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurLegal.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurLegal.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurLegal.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurLegal.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurLegal.issuingAgency':createChinese(100),  # 身份证签发机关
                   'userId':usrId    #userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'地址限制为200个字符')
        self.assertIsNone(r.json()['entity'])
#

    def test_32_allTrue(self):
        '''代办人住址为空格'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'entrepreneurAgency.realName':createChinese(20),  # 真实姓名
                   'entrepreneurAgency.sex': u'男',  # 身份证性别
                   'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
                   'entrepreneurAgency.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurAgency.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurAgency.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurAgency.cardAddress':'         ',  # 身份证的地址
                   'entrepreneurAgency.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurAgency.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurAgency.issuingAgency':createChinese(100),  # 身份证签发机关
                   'entrepreneurAgency.proxyImg': 'AAA', # 委托协议
                   'entrepreneurLegal.realName':createChinese(20),  # 真实姓名
                   'entrepreneurLegal.sex':u'男',  # 身份证性别
                   'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurLegal.birth': '1991-03-13',  # 出生
                   'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurLegal.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurLegal.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurLegal.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurLegal.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurLegal.issuingAgency':createChinese(100),  # 身份证签发机关
                   'userId':usrId    #userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'身份证的地址不能为空')
        self.assertIsNone(r.json()['entity'])

    def test_33_allTrue(self):
        '''代办人住址为特殊字符'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
            'entrepreneurAgency.realName': createChinese(20),  # 真实姓名
            'entrepreneurAgency.sex': u'男',  # 身份证性别
            'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
            'entrepreneurAgency.idNo': '41152619910313049X',  # 身份证号码
            'entrepreneurAgency.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurAgency.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurAgency.cardAddress': '~！@#￥%……&*（）——',  # 身份证的地址
            'entrepreneurAgency.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurAgency.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurAgency.issuingAgency': createChinese(100),  # 身份证签发机关
            'entrepreneurAgency.proxyImg': 'AAA',  # 委托协议
            'entrepreneurLegal.realName': createChinese(20),  # 真实姓名
            'entrepreneurLegal.sex': u'男',  # 身份证性别
            'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
            'entrepreneurLegal.birth': '1991-03-13',  # 出生
            'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
            'entrepreneurLegal.idFront': 'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
            'entrepreneurLegal.idBack': 'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
            'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
            'entrepreneurLegal.validityPeriodStartTime': '2012-04-09',  # 身份证有效期(开始时间)
            'entrepreneurLegal.validityPeriodEndTime': '2022-04-09',  # 身份证有效期（结束时间）
            'entrepreneurLegal.issuingAgency': createChinese(100),  # 身份证签发机关
            'userId': usrId  # userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

    def test_34_allTrue(self):
        '''代办人签发机关为101个字符'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'entrepreneurAgency.realName':createChinese(20),  # 真实姓名
                   'entrepreneurAgency.sex': u'男',  # 身份证性别
                   'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
                   'entrepreneurAgency.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurAgency.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurAgency.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurAgency.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurAgency.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurAgency.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurAgency.issuingAgency':createChinese(101),  # 身份证签发机关
                   'entrepreneurAgency.proxyImg': 'AAA', # 委托协议
                   'entrepreneurLegal.realName':createChinese(20),  # 真实姓名
                   'entrepreneurLegal.sex':u'男',  # 身份证性别
                   'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurLegal.birth': '1991-03-13',  # 出生
                   'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurLegal.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurLegal.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurLegal.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurLegal.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurLegal.issuingAgency':createChinese(100),  # 身份证签发机关
                   'userId':usrId    #userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'签发机关限制为100个字符')
        self.assertIsNone(r.json()['entity'])

    def test_35_allTrue(self):
        '''代办人签发机关为空'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'entrepreneurAgency.realName':createChinese(20),  # 真实姓名
                   'entrepreneurAgency.sex': u'男',  # 身份证性别
                   'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
                   'entrepreneurAgency.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurAgency.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurAgency.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurAgency.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurAgency.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurAgency.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   # 'entrepreneurAgency.issuingAgency':createChinese(101),  # 身份证签发机关
                   'entrepreneurAgency.proxyImg': 'AAA', # 委托协议
                   'entrepreneurLegal.realName':createChinese(20),  # 真实姓名
                   'entrepreneurLegal.sex':u'男',  # 身份证性别
                   'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurLegal.birth': '1991-03-13',  # 出生
                   'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurLegal.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurLegal.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurLegal.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurLegal.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurLegal.issuingAgency':createChinese(100),  # 身份证签发机关
                   'userId':usrId    #userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'身份证签发机关不能为空')
        self.assertIsNone(r.json()['entity'])

    def test_36_allTrue(self):
        '''代办人签发机关为空格'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'entrepreneurAgency.realName':createChinese(20),  # 真实姓名
                   'entrepreneurAgency.sex': u'男',  # 身份证性别
                   'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
                   'entrepreneurAgency.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurAgency.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurAgency.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurAgency.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurAgency.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurAgency.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurAgency.issuingAgency':'      ',  # 身份证签发机关
                   'entrepreneurAgency.proxyImg': 'AAA', # 委托协议
                   'entrepreneurLegal.realName':createChinese(20),  # 真实姓名
                   'entrepreneurLegal.sex':u'男',  # 身份证性别
                   'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurLegal.birth': '1991-03-13',  # 出生
                   'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurLegal.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurLegal.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurLegal.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurLegal.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurLegal.issuingAgency':createChinese(100),  # 身份证签发机关
                   'userId':usrId    #userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u'身份证签发机关不能为空')
        self.assertIsNone(r.json()['entity'])
#
    def test_37_allTrue(self):
        '''代办人签发机关为特殊字符'''
        usr = get_IdOrToken(15652000002)
        usrId = usr[0]
        usrheader = usr[2]
        content = {
                   'entrepreneurAgency.realName':createChinese(20),  # 真实姓名
                   'entrepreneurAgency.sex': u'男',  # 身份证性别
                   'entrepreneurAgency.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurAgency.cbirth': '1991-03-13',  # 出生
                   'entrepreneurAgency.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurAgency.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurAgency.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurAgency.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurAgency.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurAgency.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurAgency.issuingAgency':'~！！@#￥%……&*（）————',  # 身份证签发机关
                   'entrepreneurAgency.proxyImg': 'AAA', # 委托协议
                   'entrepreneurLegal.realName':createChinese(20),  # 真实姓名
                   'entrepreneurLegal.sex':u'男',  # 身份证性别
                   'entrepreneurLegal.ethnic': u'汉',  # 身份证的民族信息
                   'entrepreneurLegal.birth': '1991-03-13',  # 出生
                   'entrepreneurLegal.idNo': '41152619910313049X',  # 身份证号码
                   'entrepreneurLegal.idFront':'http://res.shoumeiapp.com/-4341263640.jpg',  # 身份证正面
                   'entrepreneurLegal.idBack':'http://res.shoumeiapp.com/-4340207061.jpg',  # 身份证反面
                   'entrepreneurLegal.cardAddress': createChinese(200),  # 身份证的地址
                   'entrepreneurLegal.validityPeriodStartTime':'2012-04-09',  # 身份证有效期(开始时间)
                   'entrepreneurLegal.validityPeriodEndTime':'2022-04-09',  # 身份证有效期（结束时间）
                   'entrepreneurLegal.issuingAgency':createChinese(100),  # 身份证签发机关
                   'userId':usrId    #userId
        }
        r = requests.post(url=self.url, data=content, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u'请求成功')
        self.assertIsNotNone(r.json()['entity'])

if __name__ == '__main__':
    unittest.main()