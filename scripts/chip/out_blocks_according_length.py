#!/usr/bin/env python3
# coding=utf-8
'''
@Author: Guo Yingwei
@Date: 2020-07-16 09:11:58
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-07-16 09:20:20
'''
import sys,logging,os

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")


region_d = {}
with open(sys.argv[1], 'r') as region_f:
    for line in region_f:
        lines = line.strip().split()
        if ((int(lines[2]) - int(lines[1])) // int(50000)) + 1 < 10:
            num = ((int(lines[2]) - int(lines[1])) // int(50000)) + 1
        else:
            num = 10
        #print(num)
        region_d['-'.join(lines[:3])] = num
        
for region in region_d:
    try:
        with open('TAGS/' + region + '.TAGS') as tagf:
            test = tagf.read().strip().split('Alleles Captured')[1].strip()
            d = {}
            for line in test.split('\n'):
                block = line.strip().split('\t')[1]
                d[block] = len(block.split(','))
            sort_d = sorted(d.items(),key=lambda x:x[1],reverse=True)
            blist = []
            for k, v in sort_d[:region_d[region]]:
                blist.append(k)
        with open('blocks/' + region + '.blocks', 'w') as fo:
            for block in blist:
                fo.write(block + '\n')
        fo.close()
    except:
        print('File Not Found :' + 'TAGS/' + region + '.TAGS')


