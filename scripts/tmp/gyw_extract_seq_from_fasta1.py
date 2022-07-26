# -*- coding: utf-8 -*-
"""
@author: gyw
@Date:  Wed Feb 27 20:41:41 2019
@E-mail: guoyingwei6@gmail.com
@Description: A script to extract sequences from fasta file.
"""

import sys

def usage():
    print('Usage: python3 %s [fasta_file] [idlist_file] [outfile_name]' %(sys.argv[0]))


def main():
    outf = open(sys.argv[3],'w')
    dict = {}
    with open(sys.argv[1], 'r') as fastaf:
#        n = 1
        for line in fastaf:
            if line.startswith('>'):
                name = line.strip().split()[0][1:]
                dict[name] = ''
            else:
                dict[name] += line.replace('\n','') #dict[name] += line.strip()
#                n += 1
#                print(n)

    with open(sys.argv[2],'r') as listf:
        for row in listf:
            row = row.strip()
            for key in dict.keys():
                if key == row:
                    outf.write('>' + key+ '\n')
                    outf.write(dict[key] + '\n')
                
    outf.close()


try:
    main()
except IndexError:
    usage()
