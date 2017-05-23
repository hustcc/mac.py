#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016-04-28

@author: hustcc
'''

import re
import os
import sys
import requests

try:
    import cPickle as pickle
except:
    import pickle


class Mac(object):
    def __init__(self):
        self.__parse_cnt = 0
        self.__oui_dict = {}
        self.__PY2 = sys.version_info[0] == 2
        fix = (self.__PY2 and "2") or "3"
        self.__persistence_file = os.path.normpath(os.path.join(os.path.dirname(__file__), 'oui_%s.dict' % (fix)))
        self.__raw_file = os.path.normpath(os.path.join(os.path.dirname(__file__), 'oui.txt'))

    def __process_line(self, fp, current_line):
        m = re.match(r"^[0-9A-Z]{6}", current_line)
        if m:
            self.__parse_cnt += 1
            tmp = current_line.split('\t\t')
            mac_24 = tmp[0].split('    ')[0]
            if self.__oui_dict.get(mac_24, None):
                self.__oui_dict[mac_24]['com'] += ' / ' + tmp[1].strip()
                self.__oui_dict[mac_24]['addr'] += ' / ' + fp.readline().strip()
                self.__oui_dict[mac_24]['re'] += ' / ' + fp.readline().strip()
                self.__oui_dict[mac_24]['co'] += ' / ' + fp.readline().strip()
            else:
                self.__oui_dict[mac_24] = {}
                self.__oui_dict[mac_24]['com'] = tmp[1].strip()
                self.__oui_dict[mac_24]['addr'] = fp.readline().strip()
                self.__oui_dict[mac_24]['re'] = fp.readline().strip()
                self.__oui_dict[mac_24]['co'] = fp.readline().strip()
        else:
            pass

    def _parse(self):
        '''parse the mac file, save as the serialize file. only use for dist new version
        '''
        if self.__PY2:
            oui_fp = open(self.__raw_file, 'r')
        else:
            oui_fp = open(self.__raw_file, 'r', encoding='utf8')
        while True:
            line = oui_fp.readline()
            if line:
                self.__process_line(oui_fp, line)
            else:
                break
        oui_fp.close()

        # save to file
        tmp_fp = open(self.__persistence_file, 'wb')
        pickle.dump(self.__oui_dict, tmp_fp)
        tmp_fp.close()

    def __format(self, mac):
        mac = mac or ''
        mac = mac.replace('-', '').replace(':', '')[0:6]
        mac = mac.upper()
        return mac

    def search(self, mac):
        '''search the mac address is which company
        will return a dict, has key:
        com: company name
        re: company region
        addr: company address
        co: company country'''
        mac = self.__format(mac)
        if not self.__oui_dict:
            if not os.path.exists(self.__persistence_file):
                self._parse()
            tmp_fp = open(self.__persistence_file, 'rb')
            self.__oui_dict = pickle.load(tmp_fp)
            tmp_fp.close()

        return self.__oui_dict.get(mac, None)

    def update_dictionary(self, file_path):
        """
        replace the old oui.txt with a new oui.txt to update the dictionary of mac address
        :param file_path: the file path of new oui.txt file
        :return:
        """
        source_file = open(file_path, 'rb')
        data = source_file.read()
        source_file.close()
        with open(self.__raw_file, 'wb')as f:
            f.write(data)
        self._parse()

    def update_dictionary_online(self, url='http://standards-oui.ieee.org/oui/oui.txt'):
        """
        replace the old oui.txt with a new oui.txt, which will be download from param [url]
        :param url: a http path of oui.txt on ieee.org
        :return:
        """
        print(
            """downloading 'oui.txt' from '{url}'
            that may take a long time
            please wait ……
            """.format(url=url)
        )
        r = requests.get(url)
        print("finish download")
        with open(self.__raw_file + '.new', "wb") as f:
            f.write(r.content)
        mac = Mac()
        mac.update_dictionary(self.__raw_file + '.new')
        os.remove(self.__raw_file + '.new')
        print("done")
