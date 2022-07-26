#
# -*- coding: utf-8 -*-
#Filename:   out_blocks_from_tags.py
#Author:     gyw
#Date:       2020-04-22
#

import sys,logging,os

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

with open(sys.argv[1], 'r') as tagf:
    test = tagf.read().strip().split('Alleles Captured')[1].strip()
    d = {}
    for line in test.split('\n'):
        block = line.strip().split('\t')[1]
        d[block] = len(block.split(','))
    sort_d = sorted(d.items(),key=lambda x:x[1],reverse=True)
    blist = []
    for k, v in sort_d[:3]:
        blist.append(k)
with open(sys.argv[1].replace('TAGS','blocks'), 'w') as fo:
    for block in blist:
        fo.write(block + '\n')
fo.close()
