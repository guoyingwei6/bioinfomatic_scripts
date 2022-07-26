#!/usr/bin/env python3
# coding=utf-8
'''
@Author: Guo Yingwei
@Date: 2020-07-24 12:19:10
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-07-24 12:26:10
'''

import sys,logging,os

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

fo = open(sys.argv[3], 'w')
lst = []
with open(sys.argv[1], 'r') as f2:
    for line in f2:
        lines = line.strip().split()
        lst.append(lines[0] + ':' + lines[1])
        fo.write(line)

with open(sys.argv[2], 'r') as f1:
    for line in f1:
        lines = line.strip().split()
        pos = lines[0] + ':' + lines[1]
        if pos in lst:
            continue
        else:
            fo.write(line)

fo.close()
