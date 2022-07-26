#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Guo Yingwei
Date: 2020-08-19 08:55:43
E-mail: willgyw@126.com
Description: 整理为芯片设计所需要的位点加侧翼序列的格式，需要位点的bim和提取好的两端序列。 
LastEditors: gyw
LastEditTime: 2020-08-19 10:47:58
'''

import logging
import os
import sys

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

seq_d = {}
with open(sys.argv[1], 'r') as faf:
    for line in faf:
        if line.startswith('>'):
            pos = line.strip()[1:].split(':')[0] + ':' + str(int(line.strip()[1:].split(':')[1].split('-')[0]) + 101)
            seq_d[pos] = ''
        else :
            seq_d[pos] += line.strip()

bim_d = {}
with open(sys.argv[2], 'r') as bimf:
    for line in bimf:
        lines = line.strip().split()
        bim_d[lines[1]] = '[' + lines[4] + '/' + lines[5] + ']'

fo = open(sys.argv[3], 'w')        
for k in seq_d:
    fo.write(k + ',' + seq_d.get(k, 'NAN')[:100] + bim_d.get(k, '[' + seq_d.get(k)[100] + '/N]') + seq_d.get(k, 'NAN')[101:] + '\n')

fo.close()
