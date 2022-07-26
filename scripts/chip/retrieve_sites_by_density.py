#!/usr/bin/env python3
# coding=utf-8
'''
@Author: Guo Yingwei
@Date: 2020-07-01 22:15:53
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-07-01 22:48:12
'''

import sys, os, logging

fo = open(sys.argv[3], 'w')
logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

sites_lst = []
with open(sys.argv[1], 'r') as denf:
    for line in denf:
        lines = line.strip().split()
        if 4 <= int(lines[-1]) <= 6:
            sites_lst.append(lines[0])
            
chr = '0'
pos = 0

for site in sites_lst:
    if chr == site.split(':')[0]:
        if (int(site.split(':')[1]) - pos) < int(sys.argv[2]):
            continue
        else:
            fo.write(site + '\n')
            pos = int(site.split(':')[1])
    else:
        chr = site.split(':')[0]
        pos = int(site.split(':')[1])

fo.close()

