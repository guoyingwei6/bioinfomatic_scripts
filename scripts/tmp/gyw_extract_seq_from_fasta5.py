# -*- coding: utf-8 -*-
"""
@author: gyw
@Date:  Fri Mar  1 20:16:48 2019
@E-mail: guoyingwei6@gmail.com
@Description: 
"""

import argparse


parser = argparse.ArgumentParser(description='Extract sequences from fasta file.')
parser.add_argument('--fastafile', '-f', dest='fasta', help='input a fasta file:')
parser.add_argument('--listfile', '-i', dest='idlist', help='input a idlist file:')
parser.add_argument('--outfile','-o',dest='outfile',help='input a outfile name:')        
args = parser.parse_args()

outf = open(args.outfile,'w')

dict = {}
with open(args.fasta, 'r') as fastaf:
    for line in fastaf:
        if line.startswith('>'):
            name = line.strip().split()[0][1:]
            dict[name] = ''
        else:
            dict[name] += line.replace('\n','')
        
with open(args.idlist,'r') as listf:
    for row in listf:
        row = row.strip()
        for key in dict.keys():
            if key == row:
                outf.write('>' + key+ '\n')
                outf.write(dict[key] + '\n')
                
outf.close()
