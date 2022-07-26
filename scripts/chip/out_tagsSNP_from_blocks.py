import sys,logging,os

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

'''
HiC_scaffold_31_pilon_pilon:86156907,HiC_scaffold_31_pilon_pilon:86161177
'''
fo = open(sys.argv[1].replace('blocks','tagSNP'), 'w')
with open(sys.argv[1], 'r') as blockf:
    for line in blockf:
        lines = line.strip().split(',')
        sorted_lines = sorted(lines)
        if len(sorted_lines) >= 2:
            if len(sorted_lines)%2 == 1:
                tag = sorted_lines[int((len(sorted_lines) - 1)/2)]
            else:
                tag = sorted_lines[int(len(sorted_lines)/2) - 1]
            fo.write(tag +'\n')
        else:
            tag = sorted_lines[0]
            fo.write(tag +'\n')
fo.close()
