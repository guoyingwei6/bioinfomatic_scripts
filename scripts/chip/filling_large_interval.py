#!/usr/bin/env python3
# coding=utf-8
'''
@Author: Guo Yingwei
@Date: 2020-07-17 14:37:07
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-07-24 15:45:47
'''
import sys,logging,os

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

sites_lst = []
with open(sys.argv[1], 'r') as denf:
    for line in denf:
        lines = line.strip().split()
        sites_lst.append(lines[0] + ':' + lines[1])

fo = open(sys.argv[4], 'w')
with open(sys.argv[2], 'r') as regionf:
    for line in regionf:
        tmp_lst = []
        lines = line.strip().split()        
        chrom = lines[0]
        start = int(lines[1])
        end = int(lines[2])
        for site in sites_lst:
            if chrom == site.split(':')[0]:
                if int((int(start) + int(sys.argv[3]))) <= int(site.split(':')[1]) <= end:
                    tmp_lst.append(site)
                    start = site.split(':')[1]
            else:
                continue
        fo.write('\t'.join(lines) + '\t' + str(int(end) - int(start)) + '\t' + str(len(tmp_lst)) + '\t' + ','.join(tmp_lst) + '\n')

fo.close()
