from itertools import groupby
import sys

lst = []
step= int(sys.argv[2])
fo = open(sys.argv[3], 'w')

with open(sys.argv[1], 'r') as interval:
    for line in interval:
        lines = int(line.strip())
        lst.append(lines)

for k, g in groupby(sorted(lst), key=lambda x: x//step):
    fo.write('{}-{}: {}'.format(k*step, (k+1)*step-1, len(list(g))) + '\n')
