#coding=utf-8
import unittest
import os,time
import HTMLTestRunner
import sys,unittest,requests
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\test\Desktop\jenkins\Base')
from CreatePhoneNum import *
#用例路径
print os.getcwd()    #获取当前工作目录
case_pase=os.path.join(os.getcwd(),"testcase")  #加入路径

#用例路径

report_path=os.path.join(os.getcwd(),"report")
print case_pase
def all_case():
    discover=unittest.defaultTestLoader.discover(case_pase,
                                                 pattern="test*.py",
                                                 top_level_dir=None)
    print(discover)
    return discover

if __name__=="__main__":

    # 获取当期时间，这样便于下面的使用
    now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

    # html报告存放路径
    report_abspath=os.path.join(report_path,"result_"+now+".html")

    # 打开一个文件，将result写入此file中
    fp=open(report_abspath,"ab+")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title=u'接口Zion规划测试报告，结果如下：',
                                         description=u'用例执行情况：')
    # runner=unittest.TextTestRunner()
    runner.run(all_case())
    fp.close()