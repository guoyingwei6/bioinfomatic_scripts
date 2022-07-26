# -*- coding: utf-8 -*-
"""
@author: gyw
@Date:  Fri Mar  1 09:37:13 2019
@E-mail: guoyingwei6@gmail.com
@Description: 
"""
import sys


def usage():
    print('Usage: python3 script.py [databasefile] [queryfile] [resultfile name]')
    
    
def main():
    f = open(sys.argv[1],'r',encoding='UTF-8') #编码问题
    qid = []
    res = []
    for line in f:
        qid.append(line.strip().split(',')[0]) #list.append不是list = list.append（）
        res.append(line.strip().split(',')[1])
        
    dict1 = dict(zip(qid, res))
    
    with open(sys.argv[2],'r') as qfile:
        with open(sys.argv[3],'w') as rfile:
            for row in qfile:
                row = row.strip()
                for key in dict1.keys(): #不是dict或者dict.key,而是dict.keys()
                    if row == key:
                        rfile.write(key + '\t' + dict1[key] + '\n') #是[]不是()啊！
                    

try:
    main()
except IndexError:
    usage()
