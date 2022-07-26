#!/usr/bin/env python3
# coding=utf-8
'''
@Author: Guo Yingwei
@Date: 2020-07-14 16:42:25
@E-mail: willgyw@126.com
@Description: 选取一个block当中周围SNP最密集的一个点
@LastEditors: gyw
@LastEditTime: 2020-07-14 17:02:57
'''
import sys,logging,os

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

'''
HiC_scaffold_31_pilon_pilon:86156907,HiC_scaffold_31_pilon_pilon:86161177
'''
fo = open(sys.argv[1].replace('blocks','tagSNP'), 'w')
num_d = {}
with open(sys.argv[2], 'r') as statf:
    for line in statf:
        lines = line.strip().split()
        num_d[lines[3]] = int(lines[4])

with open(sys.argv[1], 'r') as blockf:
    for line in blockf:        
        lines = line.strip().split(',')
        tag = lines[0]
        for snp in lines:
            if num_d.get(snp, 0) > 7: # 密度大于7个就舍去
                continue
            else:
                if num_d.get(snp, 0) <= num_d.get(tag, 0):
                    continue
                else:
                    tag = snp
        fo.write(tag + '\n')
        
fo.close()
                


