import sys

lst = []
with open(sys.argv[1], 'r') as nowf:
    for line in nowf:
        lst.append(line.strip().split()[0] + ':' + line.strip().split()[1])
sites_lst = []
with open(sys.argv[2], 'r') as denf:
    for line in denf:
        lines = line.strip().split()
        if 3 <= int(lines[-1]) <= 7:
            if lines[0] not in lst:
                sites_lst.append(lines[0])
fo = open(sys.argv[3], 'w')

fo.write('\n'.join(sites_lst))
