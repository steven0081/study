#coding=utf-8

import shutil, os
import re

file_dir = os.path.join('/mnt', 'download', 'TDDOWNLOAD')
file_list = os.listdir(file_dir)
#print (file_list)
for file_name in file_list:
    #name_reg = re.compile(r'(^\[电影天堂www.dy2018.com\]|^\[阳光电影www.ygdy8.net\].|^阳光电影www.ygdy8.net|^\[阳光电影www.ygdy8.com\].'
    #                      r'|^阳光电影www.ygdy8.com.)')
    name_reg = re.compile(r'(\[电影天堂www.dy2018.com\]|\[最新电影www.66ys.tv\]|.电影天堂.www.dy2018.com|\[飘花www.piaohua.com\])')
    name_replace = name_reg.sub('', file_name)
    #print(file_name)
    #print(name_replace)
    old_filename = file_dir+'/'+file_name
    new_filename = file_dir+'/'+name_replace
    #print (new_filename)
    shutil.move(old_filename, new_filename)

