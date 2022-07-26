#!/usr/bin/env python3
# coding=utf-8
'''
@Author: Guo Yingwei
@Date: 2020-08-05 10:34:19
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-08-05 10:54:25
'''

import logging
import os
import sys

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")
fo = open(sys.argv[2], 'w')

with open(sys.argv[1], 'r') as fi:
    now_chr = 0
    now_pos = 0
    tmp_line = ''
    for line in fi:
        if line.startswith('Chr'):
            continue
        else:
            lines = line.strip().split()
            if lines[0] == str(now_chr):
                interval = int(lines[1]) - int(now_pos)
                if int(interval) <=10:
                    fo.write(tmp_line + line)
                    now_pos = lines[1]
                    tmp_line = line
                else:
                    now_pos = lines[1]
                    tmp_line = line
            else:
                now_chr = lines[0]
                now_pos = lines[1]
                tmp_line = line
fo.close()                            
            
