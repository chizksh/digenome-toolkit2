# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:50:50 2015

@author: Sunghyun Kim(chizksh@gmail.com)
"""

import Levenshtein as l

def get_edit_dist(input_file, output_file, target_seq):
    fi = open (input_file,'r')
    fo = open (output_file, 'w')
    fo.write("Chr\tLocation\tForward29\tReverse29\tEdit dist for\tEdit dist rev\tStep for\tStep rev\tDeletion# for\tDeletion# rev\tBulge dist for\tBulge dist rev\n")
    for line in fi.xreadlines():
        units = line.split()
        chrm = units[0]
        loc = units[1]
        forseq = units[2]
        revseq = units[3]
        
        value = {}
        for nuc in "ATGC":
            target_seq.replace('N',nuc)
            value[nuc] = (l.distance(target_seq,forseq),l.editops(target_seq,forseq))
        for_max = max(value, key=value.get)
        for_dist, for_editops = value[for_max]
        for_step=[]        
        for each in for_editops:
            a,b,c =each
            for_step.append(a)
        for_deletion=for_step.count('delete')
        value = {}
        for nuc in "ATGC":
            target_seq.replace('N',nuc)
            value[nuc] = (l.distance(target_seq,revseq),l.editops(target_seq,revseq))
        rev_max = max(value, key=value.get)
        rev_dist, rev_editops = value[rev_max]
        rev_step=[]        
        for each in rev_editops:
            a,b,c=each
            rev_step.append(a)
        rev_deletion=rev_step.count('delete')
        #print int(rev_deletion)
        
        bulge_l = [for_dist+for_deletion*2,rev_dist+rev_deletion*2]
        del_l = [for_deletion,rev_deletion]
        fo.write(
        "%s\t%s\t\
        %s\t%s\t\
        %d\t%d\t\
        %s\t%s\t\
        %d\t%d\t\
        %d\t%d\t\
        %d\t%d\n"%
        (chrm,loc,
         forseq,revseq,
         for_dist,rev_dist,
         for_editops,rev_editops,
         for_deletion,rev_deletion,
         bulge_l[0],bulge_l[1],
         min(bulge_l),del_l[bulge_l.index(min(bulge_l))]))
        #print rev_dist+rev_deletion*4
    fi.close();fo.close()

input_files = ['./cloning_29.txt','./Oligo_29.txt']
HBB = 'CTTGCCCCACAGGGCAGTAACGG'

for input_f in input_files:
    get_edit_dist(input_f,input_f[:-4]+'_result_bulge3.txt',HBB)        
            
