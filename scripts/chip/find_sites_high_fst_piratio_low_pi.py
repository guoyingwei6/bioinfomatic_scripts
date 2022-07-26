#!/usr/bin/env python3
# coding=utf-8
'''
@Author: Guo Yingwei
@Date: 2020-07-23 10:58:10
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-07-23 20:11:10
'''

import logging
import os
import sys

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

fst_d = {}
with open(sys.argv[1], 'r') as fstf:
    for line in fstf:
        if line.startswith('CHR'):
            continue
        else:
            lines = line.strip().split()
            pos = lines[0] + ':' + lines[1]
            fst_d[pos] = lines[-1]

pi_ratio_d = {}
with open(sys.argv[2], 'r') as piratiof:
    for line in piratiof:
        lines = line.strip().split()
        pos = lines[0] + ':' + lines[1]
        pi_ratio_d[pos] = lines[-1]

pi_d = {}
with open(sys.argv[3], 'r') as pif:
    for line in pif:
        if line.startswith('CHR'):
            continue
        else:
            lines = line.strip().split()
            pos = lines[0] + ':' + lines[1]
            pi_d[pos] = lines[-1]
            
n = int(sys.argv[5])
fo = open(sys.argv[6], 'w')

with open(sys.argv[4], 'r') as regionf:
    for line in regionf:
        lines = line.strip().split()
        chr = lines[0]
        start = lines[1]
        end = lines[2]
        fst_sub_d = {}
        for k in fst_d:
            if k.split(':')[0] == chr:
                if start <= k.split(':')[1] <= end:
                    fst_sub_d[k] = float(fst_d.get(k,0))
        sorted_fst_sub_d = sorted(fst_sub_d.items(),key=lambda x:x[1],reverse=True)
        fst_sub_lst = []
        for key,value in sorted_fst_sub_d[:n]:
            fst_sub_lst.append(key)
        pi_ratio_sub_d = {}    
        for k in pi_ratio_d:
            if k.split(':')[0] == chr:
                if start <= k.split(':')[1] <= end:
                    pi_ratio_sub_d[k] = float(pi_ratio_d.get(k,0))
        sorted_pi_ratio_sub_d = sorted(pi_ratio_sub_d.items(),key=lambda x:x[1],reverse=True)
        pi_ratio_sub_lst = []
        for key,value in sorted_pi_ratio_sub_d[:n]:
            pi_ratio_sub_lst.append(key)
        pi_sub_d = {}    
        for k in pi_d:
            if k.split(':')[0] == chr:
                if start <= k.split(':')[1] <= end:
                    pi_sub_d[k] = float(pi_d.get(k))
        sorted_pi_sub_d = sorted(pi_sub_d.items(),key=lambda x: x[1],reverse=False)
        pi_sub_lst = []
        for key,value in sorted_pi_sub_d[:n]:
            pi_sub_lst.append(key)

        final_lst = list(set(fst_sub_lst).intersection(set(pi_ratio_sub_lst)).intersection(set(pi_sub_lst)))
        fo.write(line.strip() + '\t' + str(len(final_lst)) + '\t' + ','.join(final_lst) + '\n')

fo.close()        
        
