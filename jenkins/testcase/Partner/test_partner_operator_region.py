#coding=utf-8
import sys,unittest,requests
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
class get_operatorsRegion(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url='http://10.10.100.206/ucenter/region/operator/region'

    def tearDown(self):
        print u"#################自动执行测试结束##############"

    def test_01_allTrue(self):
        '''根据父类编码，查询省/直辖市下的服务商信息，'''
        content={'parentCode':120100}
        r=requests.get(url=self.url,params=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_02_allTrue(self):
        '''根子类编码，查询市/区下的服务商信息，'''
        content={'parentCode':120101}
        r=requests.get(url=self.url,params=content)
        print r.content
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

if __name__ == '__main__':
    unittest.main()


