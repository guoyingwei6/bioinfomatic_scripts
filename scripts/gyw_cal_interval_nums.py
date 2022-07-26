#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Date: 2019-02-20
#Descripton: A script to calculate the numbers of every intervals.

import click


@click.command()
@click.option('-i', '--infile', type=str, help='input a file,NO HEADER:')
@click.option('-o', '--outfile', type=click.File('w'),help='name of result:')
@click.option('-s', '--step', type=float, help='steps:')

def main(infile, outfile, step):
    """A script to calculate the numbers of every intervals."""
    res_dict = {}
    with open(infile, 'r') as i:
        for line in i:
            val = line.strip()
            if str((float(val)//float(step))*float(step)) + "-" + str((float(val)//float(step)+1)*float(step)) in res_dict:
                res_dict[str((float(val)//float(step))*float(step)) + "-" + str((float(val)//float(step)+1)*float(step))] += 1
            else:
                res_dict[str((float(val)//float(step))*float(step)) + "-" + str((float(val)//float(step)+1)*float(step))] = 1
    
    with open(outfile, 'w') as o:
        for key, value in res_dict.items():
            o.write(str(key)+"\t"+str(value)+"\n")


if __name__ == '__main__':
    main()
