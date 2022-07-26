# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Sun May  5 14:23:20 2019

@author: bpp
"""

import sys,os,logging,click
import re

logging.basicConfig(filename=os.path.basename(__file__).replace('.py','.log'),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='w')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")

def Loadgff(File):
   Dict = {}
   for line in File:
      if line.startswith('#'):continue
      else:
         line = line.strip().split('\t')
         if line[2] == 'gene':
            GeneName = re.search('(?<=Name=).*?(?=;)',line[8]).group()
            GeneID = re.search('(?<=GeneID:).*?(?=;)',line[8]).group()
            if not GeneName in Dict : Dict[GeneName] = GeneID        
   return Dict
@click.command()
@click.option('-g','--gtf',type=click.File('r'),help='GFF file',required=True)
@click.option('-l','--list',type=click.File('r'),help='Gene List file',required=True)
@click.option('-o','--output',type=click.File('w'),help='The output file',required=True)
def main(gtf,list,output):
    gtf = Loadgff(gtf)
    for gene in list:
        gene = gene.strip()
        if not gene in gtf:continue
        #output.write(gene + "\t" + gtf[gene] + "\n")
        output.write(gtf[gene] + "\n")
if __name__ == '__main__':
    main()
