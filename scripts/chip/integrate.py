import sys, os, logging


logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

anno_d = {}
fo = open(sys.argv[3], 'w')
with open(sys.argv[1], 'r') as annof:
    for line in annof:
        if line.startswith('Chr'):
            continue
        else:
            lines = line.strip().split('\t')
            anno_d[lines[0] + ':' + lines[1]] = '\t'.join(lines[3:10])
            
with open(sys.argv[2], 'r') as sitef:
    for line in sitef:
        lines = line.strip().split()
        pos = lines[0] + ':' + lines[1]
        sss = '\t'.join([lines[0], lines[1], anno_d.get(pos, (('NAN' + '\t') * 7).strip()), lines[3]])
        fo.write(sss + '\n')
        
fo.close()
