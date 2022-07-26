import sys

sites_lst = []
with open(sys.argv[1], 'r') as denf:
    for line in denf:
        lines = line.strip().split()
        if 4 <= int(lines[-1]) <= 6:
            sites_lst.append(line.strip())
            
fo = open(sys.argv[2], 'w')
fo.write('\n'.join(sites_lst))
