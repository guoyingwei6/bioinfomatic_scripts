#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: gyw
#Date: 2019-03-10
#E-mail: guoyingwei6@gmail.com
#Description:Filter reads from fastq.gz 

import filetype
import gzip
import argparse


parser = argparse.ArgumentParser(description='filter reads from fastq')
parser.add_argument('--fastq', '-f', dest='fastq', help='input a fastq file')
parser.add_argument('--idlist', '-i', dest='idlist', help='input idlist file')
parser.add_argument('--outfile', '-o', dest='outfile', help='input outfile name')
args = parser.parse_args()

fastqdict = {}
kind1 = filetype.guess(args.fastq)
kind2 = filetype.guess(args.idlist)
if kind1 is None:
    with open(args.fastq,'r') as fastq:
        for line in fastq:
            if line.startswith('@'):
                fastqid = line.strip().split()[0][1:]
                fastqdict[fastqid] = ''
            else:
                fastqdict[fastqid] += line
elif kind1.extension == 'gz':
    with gzip.open(args.fastq, 'rb') as fastq:
        for line in fastq:
            if line.decode().startswith('@'):
                fastqid = line.decode().strip().split()[0][1:]
                fastqdict[fastqid] = ''
            else:
                fastqdict[fastqid] += line.decode()

if kind1 is None:
    outfile = open(args.outfile, 'w')
elif kind1.extension == 'gz':
    outfile = gzip.open(args.outfile, 'wb')

if kind2 is None:
    with open(args.idlist, 'r') as idfile:
        for line in idfile:
            readsid = line.strip()
            for key in fastqdict.keys():
                if readsid == key:
                    res = '@' + key + '\n' + fastqdict[key]
                    if kind1 is None:
                        outfile.write(res)
                    elif kind1.extension == 'gz':
                        outfile.write(res.encode())
elif kind2.extension == 'gz':
    with gzip.open(args.idlist, 'rb') as idfile:
        for line in idfile:
            readsid = line.decode().strip()
            for key in fastqdict.keys():
                if readsid == key:
                    res = '@' + key + '\n' + fastqdict[key]
                    if kind1 is None:
                        outfile.write(res)
                    elif kind1.extension == 'gz':
                        outfile.write(res.encode())

outfile.close()
