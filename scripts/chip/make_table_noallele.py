import sys
fo = open(sys.argv[2], 'w')
mydict = {}
with open(sys.argv[1], 'r') as fastaf:
    for line in fastaf:
        if line.startswith('>'):
            name = line.strip().split()[0][1:]
            mydict[name] = ''
        else:
            mydict[name] += line.replace('\n','') #dict[name] += line.strip()

for k,v in mydict.items():
    seq = v[:100] + '[' + v[100] + '/N]' + v[101:]
    fo.write(k.split(':')[0] + ':' + str(int(k.split(':')[1].split('-')[1]) - 100) + '\t' + seq + '\n')
fo.close()
