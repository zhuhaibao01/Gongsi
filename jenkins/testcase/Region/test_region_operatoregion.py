#coding=utf-8
import sys,unittest,requests
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
class partner_region(unittest.TestCase):


    def setUp(self):
        print u"#################自动执行测试用例开始#############"
        self.url = 'http://10.10.100.206/ucenter/region/operator/region'

    def test_01_allValues(self):
        '''parentCode为0,一级'''
        content = {'parentCode':0}
        r = requests.get(url=self.url, params=content)
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_02_parentCodeNull(self):
        '''parentCoded为二级'''
        content = {'parentCode':110000}
        r = requests.get(url=self.url, params=content)
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_03_parentCodeNull(self):
        '''parentCoded为三级'''
        content = {'parentCode':110100}
        r = requests.get(url=self.url, params=content)
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def test_03_parentCodeNull(self):
        '''parentCoded为四级'''
        content = {'parentCode':110101}
        r = requests.get(url=self.url, params=content)
        print r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['success'], True)
        self.assertEqual(r.json()['message'], u"请求成功")
        self.assertIsNotNone(r.json()['entity'])

    def tearDown(self):
        print u"#################自动执行测试结束##############"

if __name__ == '__main__':
    unittest.main()


