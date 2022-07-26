#!/usr/bin/env python3
# coding=utf-8
'''
@Author: Guo Yingwei
@Date: 2020-07-13 16:42:05
@E-mail: willgyw@126.com
@Description: 计算两个群体的pi比值，没有取对数，只是比值 
@LastEditors: gyw
@LastEditTime: 2020-07-13 21:01:45
'''

import sys, os, logging

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")
fo = open(sys.argv[3], 'w')

d1 = {}
with open(sys.argv[1], 'r') as f1:
    for line in f1:
        if line.startswith('CHR'):
            continue
        else:
            lines = line.strip().split()
            if int(lines[3]) < 10:
                continue
            else:
                bin = ':'.join(lines[:3])
                pi = lines[4]
                d1[bin] = pi

d2 = {}        
with open(sys.argv[2], 'r') as f2:
    for line in f2:
        if line.startswith('CHR'):
            continue
        else:
            lines = line.strip().split()
            if int(lines[3]) < 10:
                continue
            else:
                bin = ':'.join(lines[:3])
                pi = lines[4]
                d2[bin] = pi
        
for k in d1:
    if d1.get(k, 'NAN') != 'NAN' and d2.get(k,'NAN') != 'NAN':
        ratio = float(d1.get(k, 'NAN'))/float(d2.get(k,'NAN'))
        fo.write('\t'.join(k.split(':')) + '\t' + str(round(ratio, 5)) + '\n')

fo.close()
