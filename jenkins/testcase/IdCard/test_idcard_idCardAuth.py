#coding=utf-8
import unittest, sys, os, requests, json
sys.path.append('..')
sys.path.append(os.path.abspath(os.listdir('..')[0] + '/' +'../../'))
import MySQLdb
from Base.test_CreatePhoneNum import *
import unittest
import requests
class idcard_idCardAuth(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url = 'http://10.10.100.206/ucenter/auth/idCardAuth'
        self.phone1 = AutoMysqlPhoneIsOrNo('13700000088')
        self.phone2 = AutoMysqlPhoneIsOrNo('18737665711')

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    @unittest.skipUnless(False,u'这个身份证调用过于频繁')
    def test_01_15Values(self):
        '''身份证信息全部填写正确'''
        usr = get_IdOrToken(self.phone2)
        usrId = usr[0]
        usrheader = usr[2]
        # content = u'userId='+str(usrId)+ \
        #            u'&realName=李国胜' \
        #            u'&idNo=130921199407165415' \
        #            u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
        #            u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
        #            u'&sex=男' \
        #            u'&ethnic=汉' \
        #            u'&birth=1994-07-16' \
        #            u'&cardAddress=河北省沧州市沧县大褚村乡东河头村481号' \
        #            u'&validityPeriodStartTime=2009-06-29' \
        #            u'&validityPeriodEndTime=2019-06-29' \
        #            u'&issuingAgency=乐市公安' \
        #            u'&type=C' \
        #            u'&faceRecognition=1' \
        #            u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'

        # content = u'userId='+str(usrId)+ \
        #            u'&realName=郑明开' \
        #            u'&idNo=341122199502253010' \
        #            u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
        #            u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
        #            u'&sex=男' \
        #            u'&ethnic=汉' \
        #            u'&birth=1995-02-25' \
        #            u'&cardAddress=安徽省来安县施官镇彭岗村彭南组25号' \
        #            u'&validityPeriodStartTime=2006-02-15' \
        #            u'&validityPeriodEndTime=2016-02-15' \
        #            u'&issuingAgency=市公安局思明分局' \
        #            u'&type=C' \
        #            u'&faceRecognition=1' \
        #            u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'


        content1 = u'userId='+str(usrId)+\
                   u'&realName=朱海豹' \
                   u'&idNo=41152619910313049X' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&sex=男' \
                   u'&ethnic=汉' \
                   u'&birth=1991-03-13' \
                   u'&cardAddress=河南省信阳市潢川县弋阳路办事处弋阳路4号' \
                   u'&validityPeriodStartTime=2012-04-09' \
                   u'&validityPeriodEndTime=0000-00-00' \
                   u'&issuingAgency=潢川县公安局' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNone(r.json()['entity'])

    def test_02_idNull(self):
        '''idNo为空'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content1 =  u'&realName=朱海豹' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&sex=男' \
                   u'&ethnic=汉' \
                   u'&birth=1991-03-13' \
                   u'&cardAddress=河南省信阳市潢川县弋阳路办事处弋阳路4号' \
                   u'&validityPeriodStartTime=2012-04-09' \
                   u'&validityPeriodEndTime=2022-04-09' \
                   u'&issuingAgency=潢川县公安局' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请求参数不正确")
        self.assertIsNone(r.json()['entity'])

    def test_03_realNameNull(self):
        '''realName为空'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content1 = u'userId='+str(usrId)+\
                   u'&idNo=341122199502253010' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&sex=男' \
                   u'&ethnic=汉' \
                   u'&birth=1995-02-25' \
                   u'&cardAddress=安徽省来安县施官镇彭岗村彭南组25号' \
                   u'&validityPeriodStartTime=2006-02-15' \
                   u'&validityPeriodEndTime=2016-02-15' \
                   u'&issuingAgency=市公安局思明分局' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u"请补全信息")
        self.assertIsNone(r.json()['entity'])

    def test_04_idNoNull(self):
        '''idNo为空'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content1 = u'userId='+str(usrId)+\
                   u'&realName=朱海豹' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&sex=男' \
                   u'&ethnic=汉' \
                   u'&birth=1995-02-25' \
                   u'&cardAddress=安徽省来安县施官镇彭岗村彭南组25号' \
                   u'&validityPeriodStartTime=2006-02-15' \
                   u'&validityPeriodEndTime=2016-02-15' \
                   u'&issuingAgency=市公安局思明分局' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u"请补全信息")
        self.assertIsNone(r.json()['entity'])

    def test_05_idNo19(self):
        '''idNo为19位'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content1 = u'userId='+str(usrId)+\
                   u'&realName=朱海豹' \
                   u'&idNo=1234567890123456789' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&sex=男' \
                   u'&ethnic=汉' \
                   u'&birth=1991-03-13' \
                   u'&cardAddress=河南省信阳市潢川县弋阳路办事处弋阳路4号' \
                   u'&validityPeriodStartTime=2012-04-09' \
                   u'&validityPeriodEndTime=2022-04-09' \
                   u'&issuingAgency=潢川县公安局' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],6002)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u"身份证信息不匹配")
        self.assertIsNone(r.json()['entity'])

    def test_06_idNo17(self):
        '''idNo为17位'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content1 = u'userId='+str(usrId)+\
                   u'&realName=朱海豹' \
                   u'&idNo=1234567890123456' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&sex=男' \
                   u'&ethnic=汉' \
                   u'&birth=1991-03-13' \
                   u'&cardAddress=河南省信阳市潢川县弋阳路办事处弋阳路4号' \
                   u'&validityPeriodStartTime=2012-04-09' \
                   u'&validityPeriodEndTime=2022-04-09' \
                   u'&issuingAgency=潢川县公安局' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],6002)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u"身份证信息不匹配")
        self.assertIsNone(r.json()['entity'])

    def test_07_idFontnull(self):
        '''身份证正面地址为空'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content1 = u'userId='+str(usrId)+\
                   u'&realName=朱海豹' \
                   u'&idNo=1234567890123456' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&sex=男' \
                   u'&ethnic=汉' \
                   u'&birth=1991-03-13' \
                   u'&cardAddress=河南省信阳市潢川县弋阳路办事处弋阳路4号' \
                   u'&validityPeriodStartTime=2012-04-09' \
                   u'&validityPeriodEndTime=2022-04-09' \
                   u'&issuingAgency=潢川县公安局' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u"请上传身份证正面图片")
        self.assertIsNone(r.json()['entity'])

    def test_08_idBackNull(self):
        '''idBack为空'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content1 = u'userId='+str(usrId)+\
                   u'&realName=朱海豹' \
                   u'&idNo=123456789012345678' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&sex=男' \
                   u'&ethnic=汉' \
                   u'&birth=1991-03-13' \
                   u'&cardAddress=河南省信阳市潢川县弋阳路办事处弋阳路4号' \
                   u'&validityPeriodStartTime=2012-04-09' \
                   u'&validityPeriodEndTime=2022-04-09' \
                   u'&issuingAgency=潢川县公安局' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u"请上传身份证反面图片")
        self.assertIsNone(r.json()['entity'])

    def test_08_sexNull(self):
        '''性别为空'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content1 = u'userId='+str(usrId)+\
                   u'&realName=朱海豹' \
                   u'&idNo=123456789012345678' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&ethnic=汉' \
                   u'&birth=1991-03-13' \
                   u'&cardAddress=河南省信阳市潢川县弋阳路办事处弋阳路4号' \
                   u'&validityPeriodStartTime=2012-04-09' \
                   u'&validityPeriodEndTime=2022-04-09' \
                   u'&issuingAgency=潢川县公安局' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'],False)
        self.assertEqual(r.json()['message'], u"请补全信息")
        self.assertIsNone(r.json()['entity'])

    def test_09_ethnicNull(self):
        '''民族为空'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content1 = u'userId='+str(usrId)+\
                   u'&realName=朱海豹' \
                   u'&idNo=123456789012345678' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&sex=男' \
                   u'&birth=1991-03-13' \
                   u'&cardAddress=河南省信阳市潢川县弋阳路办事处弋阳路4号' \
                   u'&validityPeriodStartTime=2012-04-09' \
                   u'&validityPeriodEndTime=2022-04-09' \
                   u'&issuingAgency=潢川县公安局' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请补全信息")
        self.assertIsNone(r.json()['entity'])

    def test_10_birthNull(self):
        '''出生地为空'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content1 = u'userId='+str(usrId)+\
                   u'&realName=朱海豹' \
                   u'&idNo=123456789012345678' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&sex=男' \
                   u'&ethnic=汉' \
                   u'&cardAddress=河南省信阳市潢川县弋阳路办事处弋阳路4号' \
                   u'&validityPeriodStartTime=2012-04-09' \
                   u'&validityPeriodEndTime=2022-04-09' \
                   u'&issuingAgency=潢川县公安局' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请补全信息")
        self.assertIsNone(r.json()['entity'])

    def test_11_cardAddressNull(self):
        '''身份证的地址为空'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content1 = u'userId='+str(usrId)+\
                   u'&realName=朱海豹' \
                   u'&idNo=123456789012345678' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&sex=男' \
                   u'&ethnic=汉' \
                   u'&birth=1991-03-13' \
                   u'&validityPeriodStartTime=2012-04-09' \
                   u'&validityPeriodEndTime=2022-04-09' \
                   u'&issuingAgency=潢川县公安局' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请补全信息")
        self.assertIsNone(r.json()['entity'])

    def test_12_cardStartTimeNull(self):
        '''身份证的开始时间为空'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content1 = u'userId='+str(usrId)+\
                   u'&realName=朱海豹' \
                   u'&idNo=123456789012345678' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&sex=男' \
                   u'&ethnic=汉' \
                   u'&birth=1991-03-13' \
                   u'&validityPeriodEndTime=2022-04-09' \
                   u'&issuingAgency=潢川县公安局' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请补全信息")
        self.assertIsNone(r.json()['entity'])

    def test_13_cardEndTime(self):
        '''身份证的截至时间为空'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content1 = u'userId='+str(usrId)+\
                   u'&realName=朱海豹' \
                   u'&idNo=123456789012345678' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&sex=男' \
                   u'&ethnic=汉' \
                   u'&birth=1991-03-13' \
                   u'&validityPeriodStartTime=2012-04-09' \
                   u'&issuingAgency=潢川县公安局' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请补全信息")
        self.assertIsNone(r.json()['entity'])

    def test_14_AgencyNull(self):
        '''身份证签发机关为空'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content1 = u'userId='+str(usrId)+\
                   u'&realName=朱海豹' \
                   u'&idNo=123456789012345678' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&sex=男' \
                   u'&ethnic=汉' \
                   u'&birth=1991-03-13' \
                   u'&validityPeriodStartTime=2012-04-09' \
                   u'&validityPeriodEndTime=2022-04-09' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请补全信息")
        self.assertIsNone(r.json()['entity'])

    def test_15_livePhotoNull(self):
        '''要添加的活体照片为空'''
        usr = get_IdOrToken(self.phone1)
        usrId = usr[0]
        usrheader = usr[2]
        content1 = u'userId='+str(usrId)+\
                   u'&realName=朱海豹' \
                   u'&idNo=123456789012345678' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&sex=男' \
                   u'&ethnic=汉' \
                   u'&birth=1991-03-13' \
                   u'&validityPeriodStartTime=2012-04-09' \
                   u'&validityPeriodEndTime=2022-04-09' \
                   u'&issuingAgency=潢川县公安局' \
                   u'&type=C' \
                   u'&faceRecognition=1'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请填写要识别的活体图片")
        self.assertIsNone(r.json()['entity'])

    def test_16_idcardUsed(self):
        '''新用户用已被认证的身份证重新进行认证'''
        usr = get_IdOrToken(e[random.randint(1,len(e)-1)])
        usrId = usr[0]
        usrheader = usr[2]
        content1 = u'userId='+str(usrId)+ \
                   u'&realName=朱海豹' \
                   u'&idNo=41152619910313049X' \
                   u'&idFront=http://res.shoumeiapp.com/-4341263640.jpg' \
                   u'&idBack=http://res.shoumeiapp.com/-4340207061.jpg' \
                   u'&sex=男' \
                   u'&ethnic=汉' \
                   u'&birth=1991-03-13' \
                   u'&cardAddress=河南省信阳市潢川县弋阳路办事处弋阳路4号' \
                   u'&validityPeriodStartTime=2012-04-09' \
                   u'&validityPeriodEndTime=2022-04-09' \
                   u'&issuingAgency=潢川县公安局' \
                   u'&type=C' \
                   u'&faceRecognition=1' \
                   u'&liveRecognitionPicture=http://res.shoumeiapp.com/-4339143682.jpg'
        r = requests.post(self.url + "?" + content1, headers=usrheader)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 6001)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"身份证已存在")
        self.assertIsNone(r.json()['entity'])

if __name__ == '__main__':
    unittest.main()

