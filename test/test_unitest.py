#-*-coding: utf-8 -*-

import unittest
try:
    from src.macpy import Mac
except:
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
        r_4 = self.mac.search('00016c')
        r_5 = self.mac.search('00')
        r_6 = self.mac.search('')
        
        self.assertEqual(r_1, r_2)
        self.assertEqual(r_2, r_3)
        self.assertEqual(r_3, r_4)
        self.assertEqual(r_4, {'re': 'Brea  CA  92821', 'com': 'FOXCONN', 'addr': '105 S Puente St.', 'co': 'US'})
        
        self.assertEqual(r_5, None)
        self.assertEqual(r_6, None)

if __name__ =='__main__':
    unittest.main()