#!/usr/bin/env python3
"""
# -*- coding: utf-8 -*-
#Date: 2019-02-24
#Description: This scripts can sort blast outfiles by Idendity.
"""

import click
from operator import itemgetter

#input_file = open('Fr_ve.outfmt6')
#output_file = open('blastoutsorted.csv', 'w')
@click.command()
@click.option('--infile', '-i', help='name of blastout file', required=True)
@click.option('--outfile', '-o', help='name of sorted file', required=True)
def main(infile, outfile):
    table = []
    with open(infile, 'r') as input_file:
        for line in input_file:
            col = line.split('\t')
            col[2] = float(col[2])
            table.append(col)

    table_sorted = sorted(table, key=itemgetter(2), reverse=True)

    with open(outfile, 'a') as output_file:
        for row in table_sorted:
            row = [str(x) for x in row]
            output_file.write('\t'.join(row))


if __name__ == '__main__':
    main()
    
