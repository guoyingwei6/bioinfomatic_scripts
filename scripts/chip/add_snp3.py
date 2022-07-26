#!/usr/bin/env python3
# coding=utf-8
'''
@Author: Guo Yingwei
@Date: 2020-07-02 20:32:25
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-07-02 22:35:25
'''
import sys, os, logging

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

fo = open(sys.argv[4], 'w')
snp_lst = []
with open(sys.argv[1], 'r') as snpf:
    for line in snpf:
        lines = line.strip().split()
        if lines[-1] == '3' or lines[-1] == '7':
            snp_lst.append(lines[0])

chr = '0'
pos = 0
with open(sys.argv[2], 'r') as sitesf:
    for line in sitesf:
        chr1 = line.strip().split(':')[0]
        pos1 = int(line.strip().split(':')[1])
        if chr == chr1:
            dist = pos1 - pos
            if dist <= int(sys.argv[3]):
                pos = pos1
            else:
                tmp_lst = []
                pos11 = pos
                for i in snp_lst:
                    if i.split(':')[0] == chr:                        
                        if (pos11 + 50000) > pos1:
                            break
                        elif pos11 < int(i.split(':')[1]) < pos1:
                            tmp_lst.append(i)
                            pos11 = int(i.split(':')[1]) + 50000
                    else:
                        continue
                fo.write(chr + ':' + str(pos) + '-' + str(pos1) + '\t' + ','.join(tmp_lst) + '\n')
                pos = pos1
        else:
            chr = chr1
            pos = pos1

fo.close()
