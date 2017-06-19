#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_layout.py
import os
import sys
import unittest
import time

import layout
yaml_data = layout.read_yaml('aikif_web1.yaml') 
 
 
class TestLayout(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.yaml_data = ''
        

    
    def test_01_read_file(self):
        """
        read the yaml file - example for use is in comments below
        """
        self.assertEqual(len(yaml_data), 6)

    
    def test_02_screen(self):
        self.assertTrue('colour_theme' in yaml_data['screen'].keys())
        self.assertTrue('max_width' in yaml_data['screen'].keys())
        self.assertTrue('max_height' in yaml_data['screen'].keys())
        
        self.assertTrue(int(yaml_data['screen']['max_width']) > 1199)
        self.assertTrue(int(yaml_data['screen']['max_height']) > 1079)
    
    def test_03_widgets(self):
        self.assertTrue(len(yaml_data['widgets']) > 4)
        self.assertTrue('nme' in yaml_data['widgets'][0].keys())
        self.assertTrue('x' in yaml_data['widgets'][0].keys())
        self.assertTrue('y' in yaml_data['widgets'][0].keys())
        self.assertTrue('w' in yaml_data['widgets'][0].keys())
        self.assertTrue('h' in yaml_data['widgets'][0].keys())
    
        self.assertTrue('Header' in yaml_data['widgets'][0]['nme'])
    

    
         
if __name__ == '__main__':
    unittest.main()
