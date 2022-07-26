'''
@Author: Guo Yingwei
@Date: 2020-06-04 16:33:51
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-06-04 16:50:07
'''
import sys,os
import logging

logging.basicConfig(filename=os.path.basename(__file__).replace('.py','.log'),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='w')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

'''
1qseqid 2sseqid 3pident 4qlen 5length 6mismatch 7gapopen 8qstart 9qend 10sstart 11send evalue bitscore qcovs
'''

fo = open(sys.argv[2], 'w')

with open(sys.argv[1], 'r') as blastf:
    for line in blastf:
        lines = line.strip().split()
        ll = 61 - int(lines[7])
        if int(lines[9]) < int(lines[10]):
            pos = int(lines[9]) + ll
        else:
            pos = int(lines[9]) - ll
        site = int(lines[0].split(':')[1].split('-')[0]) + 61
        lst = [lines[0].split(':')[0], str(site), lines[1], str(pos)]
        fo.write('\t'.join(lst) + '\n')

fo.close()
