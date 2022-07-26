import sys
fo = open(sys.argv[3], 'w')

type_d = {}
with open(sys.argv[1], 'r') as all:
    for line in all:
        if line.startswith('Chr'):
            continue
        else:
            lines = line.strip().split(',')
            type_d[lines[0] + ':' + lines[1]] = lines[2:]

with open(sys.argv[2], 'r') as need:
    for line in need:
        lines = line.strip().split(',')
        pos = lines[0] + ':' + lines[1]
        if type_d.get(pos, 'NAN')[-1] == '50K_chip':
            fo.write('\t'.join(lines) + '\t' + '\t'.join(type_d.get(pos)) + '\n')

fo.close()
