#!/usr/bin/env python3
# coding=utf-8
'''
@Author: Guo Yingwei
@Date: 2020-07-23 14:05:04
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-07-23 14:14:54
'''

import logging
import os
import sys

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

fo = open(sys.argv[3], 'w')
d1 = {}
d2 = {}
with open(sys.argv[1], 'r') as f1:
    for line in f1:
        if line.startswith('CHR'):
            continue
        else:
            lines = line.strip().split()
            d1[lines[0] + ':' + lines[1]] = float(lines[2])

with open(sys.argv[2], 'r') as f2:
    for line in f2:
        if line.startswith('CHR'):
            continue
        else:
            lines = line.strip().split()
            d2[lines[0] + ':' + lines[1]] = float(lines[2])

for k in d1:
    if k in d2:
        ratio = round(d1.get(k,'nan')/d2.get(k,'nan'), 4)
        fo.write('\t'.join(k.split(':')) + '\t' + str(ratio) + '\n')

fo.close()
