import sys,logging,os

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

fo = open(sys.argv[3], 'w')
with open(sys.argv[1], 'r') as pos:
    now_chr = '0'
    now_pos = 0
    for line in pos:
        lines = line.strip().split()
        if lines[0] == now_chr:
            interval = int(lines[1]) - int(now_pos)
            if interval > int(sys.argv[2]):
                fo.write(now_chr + '\t' + str(now_pos) + '\t' + str(lines[1]) + '\n')
                now_pos = int(lines[1])
            else:
                now_pos = int(lines[1])
        else:
            now_chr = lines[0]
            now_pos = int(lines[1])
        
fo.close()
