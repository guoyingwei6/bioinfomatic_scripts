#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: gyw
#Date: 2019-03-07
#E-mail: guoyingwei6@gmail.com
#Description:Filter reads from fastq.gz 

import gzip
import argparse


parser = argparse.ArgumentParser(description='filter reads from fastq.gz')
parser.add_argument('--fastq', '-q', dest='fastq', help='input a fastq.gz file')
parser.add_argument('--idlist', '-i', dest='idlist', help='input idlist.gz file')
parser.add_argument('--outfile', '-o', dest='outfile', help='input outfile name,end by gz')
args = parser.parse_args()

fastqdict = {}

with gzip.open(args.fastq, 'rb') as fastq:
    for line in fastq:
        if line.decode().startswith('@'):
            fastqid = line.decode().strip().split()[0][1:]
            fastqdict[fastqid] = ''
        else:
            fastqdict[fastqid] += line.decode()
   
outfile = gzip.open(args.outfile, 'wb')
       
with gzip.open(args.idlist, 'rb') as idfile:
    for line in idfile:
        readsid = line.decode().strip()
        for key in fastqdict.keys():
            if readsid == key:
                res = '@' + key + '\n' + fastqdict[key]
                outfile.write(res.encode())

outfile.close()
