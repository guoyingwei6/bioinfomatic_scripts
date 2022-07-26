# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Thu Mar 29 10:21:54 2018
@Mail: minnglee@163.com
@Author: Ming Li
"""

import sys
import os
import argparse
import time
import re
import gzip

def GetCommandLine():
    CommandLine='python3 {0}'.format(' '.join(sys.argv))
    return(CommandLine)
LogFile=None
def log(LogInfo):
    '''
    Output the LogInfo to log file
    '''
    global LogFile
    if sys.platform == 'linux':
        CurrentFolder=os.getcwd()
        LogFileName=re.split('/|\\\\',sys.argv[0].strip())
        LogFileName=LogFileName[-1].split('.')
        LogFileName='{0}/{1}.log'.format(CurrentFolder,LogFileName[0])
        if LogFile:LogFile.write(LogInfo+'\n')
        else:
            LogFile=open(LogFileName,'a')
            LogFile.write(LogInfo+'\n')
    else:
        print(LogInfo)
def LoadNameDict():
    '''
    1       NC_019458.2
    2       NC_019459.2
    '''
    Dict = {}
    for line in args.Name:
        line = line.strip().split()
        Dict[line[1]] = line[0]
    return Dict
def ChangeChromosomeNameInFastaOrGff():
    NameDict = LoadNameDict()
    GzFile = False
    if args.GzFile:
        INPUT = gzip.open(args.input,'r')
        GzFile = True
    else: 
        INPUT = open(args.input)
    if args.fasta:
        for line in INPUT:
            if GzFile: line = line.decode()
            line = line.strip()
            if line.startswith('>'):
                OldChromosomeName = line.split()[0][1:]
                if OldChromosomeName in NameDict: args.output.write('>{0}\n'.format(NameDict[OldChromosomeName]))
                else: args.output.write('>{0}\n'.format(OldChromosomeName))
            else:
                args.output.write('{0}\n'.format(line))
    elif args.gff:
        for line in INPUT:
            if GzFile: line = line.decode()
            line = line.strip()
            if line.startswith('#'):
                args.output.write('{0}\n'.format(line))
            else:
                LineList = line.split('\t')
                if LineList[0] in NameDict: args.output.write('{0}\t{1}\n'.format(NameDict[LineList[0]],'\t'.join(LineList[1:])))
                else: args.output.write('{0}\n'.format(line))
def main():
    print('Running...')
    log('The start time: {0}'.format(time.ctime()))
    log('The command line is:\n{0}'.format(GetCommandLine()))
    ChangeChromosomeNameInFastaOrGff()
    log('The end time: {0}'.format(time.ctime()))
    print('Done!')
#############################Argument
parser=argparse.ArgumentParser(description=print(__doc__),formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-i','--Input',metavar='File',dest='input',help='Input file',type=str,required=True)
parser.add_argument('--fa',dest='fasta',help='The input is fasta file',action='store_true',default=False)
parser.add_argument('--gff',dest='gff',help='The input is gff file',action='store_true',default=False)
parser.add_argument('-g','--GzFile',dest='GzFile',help='The input is gz file',action='store_true',default=False)
parser.add_argument('-N','--Name',metavar='File',dest='Name',help='Name file',type=open,required=True)
parser.add_argument('-o','--Output',metavar='File',dest='output',help='Output file',type=argparse.FileType('w'),required=True)
args=parser.parse_args()
###########################
if __name__=='__main__':
    main()
