
import sys
sys.path.append(r'F:\project\faceintertet\Commen_func')
import  faceintertest.Common_func
import  requests
import  unittest
import  json


class  wardcmp(unittest.TestCase):

     def setUp(self):

          self.w = []
          ward=faceintertest.Common_func.get_ward()
          self.datalist=ward['sysDeptDataList']
          self.status=ward['resCode']


          self.m = []
          data = faceintertest.Common_func.db_get()
          self.d=data


     def test_case1(self):
         self.lenr = len(self.datalist)
         for n in range(self.lenr):
             self.w.append(self.datalist[n]['deptName'])
         self.len1 = len(self.w)

         self.lend = len(self.d)
         for k in range(self.lend):
             if self.d[k][5] == '1':
                 self.m.append(self.d[k][1])
         self.len2 = len(self.m)


         if self.len1==self.len2:
              for n in range(self.len1):
                   for k in range(self.len2):
                        if self.w[n]==self.m[k]:
                           print(self.w[n])

         else:
               print('data error!')


     def test_case2(self):

        if self.assertEqual(self.status,'0',msg='接口调用失败')==True:
            print('接口调用成功！')



     def tearDown(self):
         print('test over!')













