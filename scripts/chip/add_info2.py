#!/usr/bin/env python3
# coding=utf-8
'''
@Author: Guo Yingwei
@Date: 2020-07-19 12:19:01
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-07-19 13:06:12
'''
import sys

info_d = {}
with open(sys.argv[1], 'r') as ggp_infof:
    for line in ggp_infof:
        if line.startswith('Chr') or line.startswith('Y') or line.startswith('AF'):
            continue
        else:
            lines = line.strip().split(',')
            if lines[4] == 'synonymous':
                info_d[lines[0] + ':' + lines[1]] = '\t'.join([lines[2], lines[3], 'exonic', lines[5], 'synonymous_SNV', lines[6]])
            elif lines[4] == 'nonsynonymous':
                info_d[lines[0] + ':' + lines[1]] = '\t'.join([lines[2], lines[3], 'exonic', lines[5], 'nonsynonymous_SNV', lines[6]])
            else:
                info_d[lines[0] + ':' + lines[1]] = '\t'.join([lines[2], lines[3], lines[4], lines[5], '.', '.'])
fo = open(sys.argv[3], 'w')
with open(sys.argv[2], 'r') as sitesf:
    for line in sitesf:
        lines = line.strip().split()
        fo.write(lines[0] + '\t' + lines[1] + '\t' + info_d.get(lines[0] + ':' + lines[1], (('NAN' + '\t')*6).strip('\t')) + '\t' + lines[-1] + '\n')

fo.close() 
