#!/usr/bin/env python3
# coding=utf-8
'''
@Author: Guo Yingwei
@Date: 2020-06-30 10:47:49
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-06-30 16:29:37
'''

import sys, os, logging


logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

sites_lst = []
snp_lst = []
fo = open(sys.argv[3], 'w')

with open(sys.argv[1], 'r') as sitesf:
    for line in sitesf:
        sites_lst.append(line.strip())

with open(sys.argv[2], 'r') as mapf:
    for line in mapf:
        lines = line.strip().split()
        snp_lst.append(lines[1])

for site in sites_lst:
    num = 0
    for snp in snp_lst:
        if snp.split(':')[0] == site.split(':')[0]:
            if int(snp.split(':')[1]) < (int(site.split(':')[1]) - 100):
                continue
            elif (int(site.split(':')[1]) - 100) <= int(snp.split(':')[1]) <= (int(site.split(':')[1]) + 100):
                num += 1
            elif int(snp.split(':')[1]) > (int(site.split(':')[1]) + 100):
                break
        else:
            continue
    fo.write(site + '\t' + str(num) + '\n')

fo.close()
