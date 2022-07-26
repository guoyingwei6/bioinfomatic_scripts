import sys, os, logging


logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

with open(sys.argv[1], 'r') as fi:    
    a, b = 0, 0
    for line in fi:
        lines = line.strip().split()     
        if a == lines[0] and b == lines[1]:
            print(line.strip())
        else:
            a = lines[0]
            b = lines[1]
