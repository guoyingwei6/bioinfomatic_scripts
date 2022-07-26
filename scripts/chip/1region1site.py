'''
@Author: Guo Yingwei
@Date: 2020-06-28 15:02:47
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-06-28 15:11:28
'''
import sys, os, logging


logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")
'''
2   131322022   litter size
26  40945519    litter size
2   131323179   litter size
2   131323506   litter size
9   20392108    litter size
'''
fo = open(sys.argv[2], 'w')
with open(sys.argv[1], 'r') as fi:
    a = 0
    for line in fi:
        lines = line.strip().split(',')
        if a == lines[0]:
            continue
        else:
            fo.write('\t'.join(lines) + '\n')
            a = lines[0]
fo.close()

