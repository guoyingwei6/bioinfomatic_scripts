# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 23:46:57 2019

@author: YP
"""

import click

@click.command()
@click.argument("input")
@click.argument("output")

def CountFa(input,output):
    SeqName = ""
    SeqCount = ""
    infile = open(input,"r")
    outfile = open(output,"w")
    for line in infile.readlines():
        line = line.strip()
        if line.startswith(">") and SeqCount == "":
            try:
                SeqName = line.split(" ",1)[0][1:]
            except:
                SeqName = line[1:]
        elif line.startswith(">") and SeqCount != "":
            outfile.write(SeqName +"\t0\t" + str(len(SeqCount)) + "\n")
            try:
                SeqName = line.split(" ",1)[0][1:]
            except:
                SeqName = line[1:]
            SeqCount = ""
        elif line[0] != ">":
            SeqCount +=  line
    outfile.write(SeqName +"\t0\t" + str(len(SeqCount)) + "\n")   

if __name__ == "__main__":
     CountFa()       
