#!/usr/bin/env python

import unittest
import kata1

class testProblem01(unittest.TestCase):

    mydata = None
    result = None

    def testP01(self):
        self.assertEqual(kata1.problem01(self.mydata), self.result)


class testProblem02(unittest.TestCase):

    mydata = '12-13-14,45-156-23,234-234-256' 
    result = '#0C0D0E,#2D9C17,INVALID'

    def testP02(self):
        self.assertEqual(kata1.problem02(self.mydata), self.result)


class testProblem03(unittest.TestCase):

    low_value = 1000
    high_value = 1200   # the module ensures that this is inclusive
    result = '1001,1008,1022,1029,1036,1043,1057,1064,1071,1078,1092,1099,1106,1113,1127,1134,1141,1148,1162,1169,1176,1183,1197' 

    def testP03(self):
        self.assertEqual(kata1.problem03(self.low_value, self.high_value), 
                           self.result)


class testProblem04(unittest.TestCase):

    mydata = 'order,hello,would,test'
    result = 'hello,order,test,would'

    def testP04(self):
        self.assertEqual(kata1.problem04(self.mydata), self.result)


class testProblem05(unittest.TestCase):
    
    knownValues = ( ('305', 20400),
                    ('180', 11600),
                    ('120', 7400)
                   )

    def testP05(self):
        for reading, charge in self.knownValues:
            self.assertEqual(kata1.problem05(reading), 
                                              charge)


class testProblem06(unittest.TestCase):

    mydata = '0011,0100,0101,1001' 
    result = '0011,1001' 

    def testP06(self):
        self.assertEqual(kata1.problem06(self.mydata), self.result)


class testProblem07(unittest.TestCase):

    mydata = ('2,2','2,3','3,3','3,4')
    result = ( [[1, 2], [3, 4]],[[1, 2, 3], [4, 5, 6]],
               [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
               [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
               )

    def testP07(self):
        for parms, output in zip(self.mydata, self.result):
            self.assertEqual(kata1.problem07(parms), output)


class testProblem08(unittest.TestCase):

    mydata = '2,5,8'
    result = '98,99995,99999992'

    def testP08(self):
        self.assertEqual(kata1.problem08(self.mydata), self.result)


class testProblem09(unittest.TestCase):

    mydata = '100,150,180'
    result = '18,22,24' 

    def testP09(self):
        self.assertEqual(kata1.problem09(self.mydata), self.result)


class testProblem10(unittest.TestCase):

    mydata = 'Abc@1,a B1#,2w3E*,2We#3345'
    result = 'Abc@1,2w3E*'

    def testP10(self):
        self.assertEqual(kata1.problem10(self.mydata), self.result)

if __name__ == '__main__':
    unittest.main()
