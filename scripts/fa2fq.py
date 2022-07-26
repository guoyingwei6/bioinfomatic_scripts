'''
@Author: Guo Yingwei
@Date: 2019-09-12 10:45:20
@E-mail: willgyw@126.com
@Description: fasta to fastq
@Usuage: python3 fa2fq.py gz.fa gz.fq
@LastEditors: Do not edit
@LastEditTime: 2019-10-09 22:50:03
@Debug: Well, it can use with fasta file with mutilines now, though it has redundent codes.
'''

import gzip
import sys

outf = gzip.open(sys.argv[2], 'wb')
with gzip.open(sys.argv[1], 'rb') as inf:
    chdu = 0
    seq = ''
    for line in inf:
        line = line.decode()
        if line.startswith('>') and seq == "":
            id = line.replace('>', '@')
        if not line.startswith('>'):
            chdu += len(line.strip())
            seq += line.strip()
            s = '\n' + '+' + '\n' + r'#'*chdu + '\n'
        if line.startswith('>') and seq != "":
            outf.write(id.encode() + seq.encode() + s.encode())
            chdu = 0
            seq = ''
            id = line.replace('>', '@')
    outf.write(id.encode() + seq.encode() + s.encode())
outf.close()
