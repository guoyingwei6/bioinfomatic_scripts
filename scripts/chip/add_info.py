#!/usr/bin/env python3
# coding=utf-8
'''
@Author: Guo Yingwei
@Date: 2020-07-19 11:51:44
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-07-19 12:04:28
'''

import sys,logging,os

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

anno_d = {}
with open(sys.argv[1], 'r') as annof:
    for line in annof:
        if line.startswith('Chr'):
            continue
        else:
            lines = line.strip().split()
            anno_d[lines[0] + ':' + lines[1]] = '\t'.join([ lines[3], lines[4], lines[5], lines[6], lines[8], lines[9]])
fo = open(sys.argv[3], 'w')            
with open(sys.argv[2], 'r') as sitesf:
    for line in sitesf:
        lines = line.strip().split()        
        fo.write(lines[0] + '\t' + lines[1] + '\t' + anno_d.get(lines[0] + ':' + lines[1], (('NAN' + '\t')*6).strip('\t')) + '\t' + lines[2] + '\n')

fo.close()
