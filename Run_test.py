import  time
from HtmlTestRunner import HTMLTestReport
import sys
import  unittest
import  os

test_dir=r'./faceintertest'

file=unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__=='__main__':
    now=time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
    path= os.path.dirname(os.path.abspath(sys.argv[0]))
    filename=path+'\\report\\'+now+'report.html'
    fp=open(filename,'wb')
    runner = HTMLTestReport.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        #description='详细测试用例结果',
        tester='penglai'
        )

    runner.run(file)
    fp.close()


