# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:47:07 2015

@author: Irshad
"""

from string import maketrans
from string import atoi
trans = maketrans("ATGC","TACG")

def get_29bp(input_file_name, output_file_name):
    fi = open(input_file_name,'r')
    fo = open(output_file_name,'w')
    chr_seq = []
    l = range(1,23); l.append('X')
    
    for i in l:
        f_chr = open("./chromosome_data/chr"+str(i)+".fa", 'r')
        chr_seq.append(f_chr.read()) #chr1:chr_seq[0], chrX:chr_seq[22]
        f_chr.close()
    
    for line in fi.xreadlines():
        units = line.split()
        chrm = units[0]
        loc = int(units[1])
        
        
        if chrm == 'chrX':
            result1 = chr_seq[22][loc-23:loc+6]
            result2 = (chr_seq[22][loc-9:loc+20]).translate(trans)[::-1]
        else:
            result1 = chr_seq[atoi(chrm[3:])-1][loc-23:loc+6]
            result2 = (chr_seq[atoi(chrm[3:])-1][loc-9:loc+20]).translate(trans)[::-1]
        fo.write("%s\t%s\t%s\t%s\n"%(units[0],units[1],result1,result2))
        
    
    fi.close()
    fo.close()


files = ['./clonging.txt','./Oligo.txt']
for each in files:
    input_file_name = each
    output_file_name = each[:-4]+'_29.txt'
    get_29bp(input_file_name,output_file_name)

