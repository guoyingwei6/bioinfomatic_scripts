#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Guo Yingwei
Date: 2020-08-20 22:29:28
E-mail: willgyw@126.com
Description:  统计每条染色体上的位点间距
LastEditors: gyw
LastEditTime: 2020-08-20 22:56:50
'''
import logging
import os
import sys
import numpy as np

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

dist_d = {}
with open(sys.argv[1], 'r') as fi:
    tmp_chr = '0' 
    tmp_pos = 0
    lst =  [] 
    for line in fi:        
        if line.startswith('Chr'):
            continue
        else:
            lines = line.strip().split()
            chr = lines[0]
            pos = int(lines[1])
            if chr == tmp_chr:
                dist = int(pos) - int(tmp_pos)
                lst.append(dist)
                tmp_pos = pos
            else:
                if tmp_chr != '0':
                    dist_d[tmp_chr] = lst #buenngzhijieqingkong
                tmp_chr = chr
                tmp_pos = pos
                lst =  []
            dist_d[tmp_chr] = lst
with open(sys.argv[2], 'w') as fo:
    for k in dist_d:
        aver = np.mean(dist_d.get(k))
        fo.write(str(k) + '\t' + str(round(aver, 2)) + '\n')
fo.close()
