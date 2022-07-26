# -*- coding: utf-8 -*-
"""
@author: Guo Yingwei
@Date:  Thu May 30 16:51:51 2019
@E-mail: guoyingwei6@gmail.com
@Description: cut fasta 500bp  | python3 sys.argv[0] fasta 500bp.fa
"""


import sys


seq = {}
res = open(sys.argv[2], 'w')
with open(sys.argv[1], 'r') as fa:
    for line in fa:
        if line.startswith('>'):
            name = line.strip().split()[0][1:]
            seq[name] = ''
        else:
            seq[name] += line.replace('\n', '')
            
for k, v in seq.items():
    if len(v) <= 500:
        res.write('>' + k+ '\n' + v + '\n')
    else:
        res.write('>' + k+ '\n' + v[:500] + '\n')
