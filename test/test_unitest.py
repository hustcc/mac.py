#-*-coding: utf-8 -*-

import unittest, time
import sys, random
from macpy import Mac


class TestCase(unittest.TestCase):
    ## init
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.mac = Mac()
        
    # exit
    def tearDown(self):
        pass
    
    # test search method
    def test_search_mac(self):
        r_1 = self.mac.search('00016C')
        r_2 = self.mac.search('00:01:6C:06:A6:29')
        r_3 = self.mac.search('00-01-6C-06-A6-29')
        r_4 = self.mac.search('00')
        r_5 = self.mac.search('')
        
        self.assertDictEqual(r_1, r_2)
        self.assertDictEqual(r_2, r_3)
        self.assertDictEqual(r_3, {'re': 'Brea  CA  92821', 'com': 'FOXCONN', 'addr': '105 S Puente St.', 'co': 'US'})
        
        self.assertIsNone(r_4)
        self.assertIsNone(r_5)

if __name__ =='__main__':
    unittest.main()