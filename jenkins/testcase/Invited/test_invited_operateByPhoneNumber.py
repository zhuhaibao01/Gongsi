#coding=utf-8
import unittest
import requests
import unittest, sys, os, requests, json
sys.path.append('..')
sys.path.append(os.path.abspath(os.listdir('..')[0] + '/' +'../../'))
import MySQLdb
from Base.test_CreatePhoneNum import *
# Y 服务商， H 新媒人， C 个人， B企业主
class member_getInvitedCodeInfo(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url = 'http://10.10.100.206/ucenter/invited/operateByPhoneNumber'
        self.phone11 = AutoMysqlPhoneIsOrNo('13700000011')
        self.Entrephone = AutoMysqlPhoneIsOrNo('13919273370')
        self.Hphone = AutoMysqlPhoneIsOrNo('13700000008')
        self.Yphone = AutoMysqlPhoneIsOrNo('15652002619')
        self.Registphone = AutoMysqlPhoneIsOrNo('13700000031')
        self.noRegphone=int(C(sql(allSql()['sql1'])))
        self.exitphton=sql(allSql()['sql1'])[random.randint(1,len(allSql()['sql1']))]

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''新媒人邀请未注册的首媒用户成为C端用户'''
        content = {'userId':1613,        #邀请人的usrId
                   'inviterStatus': 'H',  #邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'C', #被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': self.noRegphone,
                   'code': 100005}
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 7020)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请先注册成为首媒用户")
        self.assertIsNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''新媒人邀请未注册的首媒用户成为企业主'''
        content = {'userId': 1613,  # 邀请人的usrId
                   'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': self.noRegphone,
                   'code': 100005}
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 7020)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请先注册成为首媒用户")
        self.assertIsNone(r.json()['entity'])

    def test_03_allTrue(self):
        '''新媒人邀请未注册的首媒用户成为新媒人'''
        content = {'userId': 1613,  # 邀请人的usrId
                   'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'H',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': self.noRegphone,
                   'code': 100005}
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 7020)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请先注册成为首媒用户")
        self.assertIsNone(r.json()['entity'])

    def test_04_allTrue(self):
        '''新媒人邀请未注册的首媒用户成为服务商'''
        content = {'userId': 1613,  # 邀请人的usrId
                   'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'Y',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': self.noRegphone,
                   'code': 100005}
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请类型 为  C  H  B")
        self.assertIsNone(r.json()['entity'])

    def test_05_allTrue(self):
        '''新媒人邀请已注册的普通首媒用户成为企业主'''
        content = {'userId':'1613',       #邀请人的usrId
                   'inviterStatus': 'H',  #邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'B', #被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': 13700000004,
                   'code': 100005}
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNone(r.json()['entity'])
    #
    def test_06_allTrue(self):
        '''新媒人邀请已注册的普通首媒用户成为新媒人'''
        content = {'userId': '1613',  # 邀请人的usrId
                   'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'H',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': self.exitphton,
                   'code': 100005}
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请求参数不正确")
        self.assertIsNone(r.json()['entity'])

    def test_07_allTrue(self):
        '''新媒人邀请已注册的普通首媒用户成为服务商'''
        content = {'userId': '1613',  # 邀请人的usrId
                   'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'Y',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile':self.exitphton,
                   'code': 100005}
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请类型 为  C  H  B")
        self.assertIsNone(r.json()['entity'])

    def test_08_allTrue(self):
        '''新媒人邀请企业主成为企业主'''
        content = {'userId': '1613',  # 邀请人的usrId
                   'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': '13919273370',
                   'code': 100005}
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 7019)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请者企业主已激活")
        self.assertIsNone(r.json()['entity'])

    def test_09_allTrue(self):
        '''新媒人邀请企业主成为新媒人'''
        content = {'userId': '1613',  # 邀请人的usrId
                   'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'H',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': '13919273370',
                   'code': 100005}
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请求参数不正确")
        self.assertIsNone(r.json()['entity'])

    def test_10_allTrue(self):
        '''新媒人邀请企业主成为服务商'''
        content = {'userId': '1613',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'Y',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile':'13919273370',
                   'code': 100005}
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请类型 为  C  H  B")
        self.assertIsNone(r.json()['entity'])

    def test_11_allTrue(self):
        '''新媒人邀请新媒人成为企业主'''
        content = {'userId': '1613',  # 邀请人的usrId
                   'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile':'13700000088',
                   'code': 100005}
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNone(r.json()['entity'])

    def test_12_allTrue(self):
        '''新媒人邀请新媒人成为新媒人'''
        content = {'userId': '1613',  # 邀请人的usrId
                   'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'H',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': '13700000088',
                   'code': 100005}
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请求参数不正确")
        self.assertIsNone(r.json()['entity'])

    def test_13_allTrue(self):
        '''新媒人邀请新媒人成为服务商'''
        content = {'userId': '1613',  # 邀请人的usrId
                   'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'Y',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile':'13700000088',
                   'code': 100005}
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请类型 为  C  H  B")
        self.assertIsNone(r.json()['entity'])

    def test_14_allTrue(self):
        '''新媒人邀请服务商成为企业主'''
        content = {'userId': '1613',  # 邀请人的usrId
                   'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': 15652002619,
                   'code': 100005
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNone(r.json()['entity'])

    def test_15_allTrue(self):
        '''新媒人邀请服务商成为新媒人'''
        content = {'userId': '1613',  # 邀请人的usrId
                   'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'H',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile':'15652002619',
                   'code': 100005
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'],u"请求参数不正确")
        self.assertIsNone(r.json()['entity'])

    def test_16_allTrue(self):
        '''新媒人邀请服务商成为服务商'''
        content = {'userId': '1613',  # 邀请人的usrId
                   'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'Y',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': 15652002619,
                   'code': 100005
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请类型 为  C  H  B")
        self.assertIsNone(r.json()['entity'])

    def test_17_allTrue(self):
        '''服务商邀请未注册用户成为C端用户'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'C',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': self.noRegphone,
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 7020)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请先注册成为首媒用户")
        self.assertIsNone(r.json()['entity'])

    def test_18_allTrue(self):
        '''服务商邀请未注册用户成为企业主'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': self.noRegphone,
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 7020)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请先注册成为首媒用户")
        self.assertIsNone(r.json()['entity'])

    def test_19_allTrue(self):
        '''服务商邀请未注册用户成为新媒人'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'H',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': self.noRegphone,
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 7020)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请先注册成为首媒用户")
        self.assertIsNone(r.json()['entity'])

    def test_20_allTrue(self):
        '''服务商邀请未注册用户成为服务商'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'Y',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': self.noRegphone,
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请类型 为  C  H  B")
        self.assertIsNone(r.json()['entity'])

    def test_21_allTrue(self):
        '''服务商邀请已注册普通用户成为企业主'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile':'13700000004',
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNone(r.json()['entity'])

    def test_22_allTrue(self):
        '''服务商邀请已注册普通用户成为新媒人'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'H',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': self.exitphton,
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNone(r.json()['entity'])

    def test_23_allTrue(self):
        '''服务商邀请已注册普通用户成为服务商'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'Y',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': self.exitphton,
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请类型 为  C  H  B")
        self.assertIsNone(r.json()['entity'])

    def test_24_allTrue(self):
        '''服务商邀请企业主成为企业主'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile':'13919273370',
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],7019)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请者企业主已激活")
        self.assertIsNone(r.json()['entity'])

    def test_25_allTrue(self):
        '''服务商邀请企业主成为新媒人'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'H',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': '13919273370',
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNone(r.json()['entity'])

    def test_26_allTrue(self):
        '''服务商邀请企业主成为服务商'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'Y',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': '13919273370',
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请类型 为  C  H  B")
        self.assertIsNone(r.json()['entity'])

    def test_27_allTrue(self):
        '''服务商邀请新媒人成为企业主'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': '13700000088',
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNone(r.json()['entity'])

    def test_28_allTrue(self):
        '''服务商邀请新媒人成为新媒人'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'H',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': '13700000088',
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 7012)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请者已经是新媒人")
        self.assertIsNone(r.json()['entity'])

    def test_29_allTrue(self):
        '''服务商邀请新媒人成为服务商'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'Y',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': '13700000088',
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请类型 为  C  H  B")
        self.assertIsNone(r.json()['entity'])

    def test_30_allTrue(self):
        '''服务商邀请服务商成为企业主'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': '15652002619',
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNone(r.json()['entity'])

    def test_31_allTrue(self):
        '''服务商邀请服务商成为新媒人'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'H',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': '15652002619',
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNone(r.json()['entity'])

    def test_32_allTrue(self):
        '''服务商邀请服务商成为服务商'''
        content = {'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'Y',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': '15652002619',
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请类型 为  C  H  B")
        self.assertIsNone(r.json()['entity'])

    def test_33_allTrue(self):
        '''userId为空'''
        content = {
                   # 'userId': '690',  # 邀请人的usrId
                   'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
                   'beInvitedStatus': 'H',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
                   'userMobile': '15652002619',
                   'code': 123457
                   }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"邀请人的userId不能为空")
        self.assertIsNone(r.json()['entity'])

    def test_34_allTrue(self):
        '''userId与inviterStatus不匹配'''
        content = {
            'userId': '1613',  # 邀请人的usrId
            'inviterStatus': 'Y',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 'H',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': '15652002619',
            'code': 100005
        }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请求参数不正确")
        self.assertIsNone(r.json()['entity'])

    @unittest.skip(u'不需要此次用例')
    def test_35_allTrue(self):
        '''userId为字母或汉字'''
        content = {
            'userId': 'woshi',  # 邀请人的usrId
            'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': '15652002619',
            'code': 100005
        }
        r = requests.post(url=self.url, data=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请求参数不正确")
        self.assertIsNone(r.json()['entity'])

    @unittest.skip(u'不需要此次用例')
    def test_36_allTrue(self):
        '''userId为特殊字符'''
        content = {
            'userId': '~！@#￥%……&',  # 邀请人的usrId
            'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': '15652002619',
            'code': 100005
        }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"请求参数不正确")
        self.assertIsNone(r.json()['entity'])

    @unittest.skip(u'不需要此次用例')
    def test_37_allTrue(self):
        '''inviterStatus为除了H,Y的任意字母'''
        content = {
            'userId': '1613',  # 邀请人的usrId
            'inviterStatus': 'qq',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': '15652002619',
            'code': 100005
        }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"邀请人类型  只能为H或者Y")
        self.assertIsNone(r.json()['entity'])

    def test_38_allTrue(self):
        '''inviterStatus为汉字'''
        content = {
            'userId': '1613',  # 邀请人的usrId
            'inviterStatus': u'汉字',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': '15652002619',
            'code': 100005
        }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"邀请人类型  只能为H或者Y")
        self.assertIsNone(r.json()['entity'])

    def test_39_allTrue(self):
        '''beInviterStatus为数字'''
        content = {
            'userId': '1613',  # 邀请人的usrId
            'inviterStatus':'H',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 123,  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': '15652002619',
            'code': 100005
        }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请类型 为  C  H  B")
        self.assertIsNone(r.json()['entity'])

    def test_40_allTrue(self):
        '''beInviterStatus为汉字'''
        content = {
           'userId': '1613',  # 邀请人的usrId
           'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
           'beInvitedStatus':u'我是汉字',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
           'userMobile': '15652002619',
           'code': 100005
        }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请类型 为  C  H  B")
        self.assertIsNone(r.json()['entity'])

    def test_41_allTrue(self):
        '''beInviterStatus为除了C、H、B之外的其他字母'''
        content = {
            'userId': '1613',  # 邀请人的usrId
            'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 'K',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': '15652002619',
            'code': 100005
        }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"被邀请类型 为  C  H  B")
        self.assertIsNone(r.json()['entity'])

    def test_42_allTrue(self):
        '''userMobile为汉字'''
        content = {
            'userId': '1613',  # 邀请人的usrId
            'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': u'我是一个十一位的汉字哦',
            'code': 100005
        }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"手机格式错误")
        self.assertIsNone(r.json()['entity'])

    def test_43_allTrue(self):
        '''userMobile为超出11位的数字'''
        content = {
            'userId': '1613',  # 邀请人的usrId
            'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': 156520026191,
            'code': 100005
        }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"手机号长度11位")
        self.assertIsNone(r.json()['entity'])

    def test_44_allTrue(self):
        '''userMobile为9位的数字'''
        content = {
            'userId': '1613',  # 邀请人的usrId
            'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': 1565200261,
            'code': 100005
        }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"手机格式错误")
        self.assertIsNone(r.json()['entity'])

    def test_45_allTrue(self):
        '''邀请码为5位的数字'''
        content = {
            'userId': '1613',  # 邀请人的usrId
            'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': 15652002619,
            'code': 10000
        }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"邀请码长度错误")
        self.assertIsNone(r.json()['entity'])

    def test_46_allTrue(self):
        '''邀请码为12位的数字'''
        content = {
            'userId': '1613',  # 邀请人的usrId
            'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': 15652002619,
            'code': 123456789012
        }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"邀请码长度错误")
        self.assertIsNone(r.json()['entity'])

    def test_47_allTrue(self):
        '''邀请码为12位的数字'''
        content = {
            'userId': '1613',  # 邀请人的usrId
            'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': 15652002619,
            'code': 123456789012
        }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"邀请码长度错误")
        self.assertIsNone(r.json()['entity'])

    def test_48_allTrue(self):
        '''邀请码为6位的汉字'''
        content = {
            'userId': '1613',  # 邀请人的usrId
            'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': 15652002619,
            'code': u'我是六位汉字'
        }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"邀请码格式错误")
        self.assertIsNone(r.json()['entity'])

    def test_49_allTrue(self):
        '''邀请码为6位的特殊字符'''
        content = {
            'userId': '1613',  # 邀请人的usrId
            'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': 15652002619,
            'code': '~！@#￥%…&'
        }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"邀请码格式错误")
        self.assertIsNone(r.json()['entity'])

    def test_50_allTrue(self):
        '''邀请码为6位的空格'''
        content = {
            'userId': '1613',  # 邀请人的usrId
            'inviterStatus': 'H',  # 邀请人类型 只能为H或者Y
            'beInvitedStatus': 'B',  # 被邀请类型 H的下线为 C或者B Y的下线为 C H B
            'userMobile': 15652002619,
            'code': '      '
        }
        r = requests.post(url=self.url, data=content)
        print r.status_code
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.json()['code'], 2000)
        self.assertEqual(r.json()['success'], False)
        self.assertEqual(r.json()['message'], u"邀请码格式错误")
        self.assertIsNone(r.json()['entity'])

if __name__=='__main__':
    unittest.main()