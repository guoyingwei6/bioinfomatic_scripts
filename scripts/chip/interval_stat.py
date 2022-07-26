'''
Scaffold319 360
X   210761
X   212024
'''
import sys

fo = open(sys.argv[2], 'w')
with open(sys.argv[1], 'r') as pos:
    now_chr = 0
    now_pos = 0
    for line in pos:
        lines = line.strip().split()
        if lines[0] == str(now_chr):
            interval = int(lines[1]) - int(now_pos)
            fo.write(str(interval) + '\n')
            now_chr = lines[0]
            now_pos = lines[1]
        else:
            now_chr = lines[0]
            now_pos = lines[1]

fo.close()
