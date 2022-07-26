# -*- coding: utf-8 -*-
"""
@author: gyw
@Date:  Wed Feb 27 09:19:54 2019
@E-mail: guoyingwei6@gmail.com
@Description: This program can extract sequences 
              from a fasta file, according to a 
              given id list.
"""

import fire


def main(fastafile, idfile, outfile):
    """
    Extract seqences from a fasta file 
    according to a id list.
    """
    idfile = open(idfile, 'r')
    resultfile = open(outfile, 'w')
    for id in idfile:
        qid = id.strip()
        flag = 0
        with open(fastafile,'r') as ffile:
            for line in ffile:
                line = line.strip()
                if line.startswith('>'):
                    name = line.replace('>','').split()[0]
                    if name == qid:
                        flag = 1
                        resultfile.write(line + '\n')
                    else:
                        flag = 0
                else:
                    if flag == 0:
                        pass
                    else:
                        resultfile.write(line + '\n')
    resultfile.close()


fire.Fire(main)
