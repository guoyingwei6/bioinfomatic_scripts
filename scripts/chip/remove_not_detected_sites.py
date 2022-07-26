#!/usr/bin/env python3
# coding=utf-8
'''
@Author: Guo Yingwei
@Date: 2020-07-17 21:09:46
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-07-17 21:15:16
'''

import sys,logging,os

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

not_lst = []
with open(sys.argv[1], 'r') as notf:
    for line in notf:
        lines = line.strip().split()
        not_lst.append(lines[0] + ':' + lines[1])
fo = open(sys.argv[3], 'w')
foo = open(sys.argv[4], 'w')
with open(sys.argv[2], 'r') as sitesf:
    for line in sitesf:
        lines = line.strip().split()
        pos = lines[0] + ':' + lines[1]
        if pos in not_lst and lines[2] != 'important_genes':
            foo.write(line)
        else:
            fo.write(line)
fo.close()
