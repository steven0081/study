#coding=utf-8

import shutil, os
import re

file_dir = os.path.join('/mnt', 'download', 'TDDOWNLOAD')
file_list = os.listdir(file_dir)
#print (file_list)
for file_name in file_list:
    name_reg = re.compile(r'阳光电影www.ygdy8.net*|阳光电影www.ygdy8.com.*')
    name_replace = name_reg.sub('', file_name)
    print(file_name)
    print(name_replace)
    '''
    file = file_dir+ '/' + file_name
    if os.path.isfile(file):
        print(file)
    '''
