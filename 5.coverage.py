import sys
import re
import pysam
from sys import argv # argv[1]: prefix, argv[2]: PATH of BAM file
from os import path



linechunk = []
prev_pos = -1
prev_chrom = ""

depth_dic = {}

def process_chunk(linechunk):
    for chrom, pos, cigar in linechunk:
        cur_pos = pos
        pos_back = 0
        leftflag = True
        for s, n in cigar:
            if not leftflag or (s != 4 and s != 5):
                for pos_diff in range(n):
                    if (s != 1 and s != 4 and s != 5):
                        if (cur_pos-pos_back) in depth_dic:
                            depth_dic[cur_pos-pos_back] += 1
                        else:
                            depth_dic[cur_pos-pos_back] = 1
                    if s == 1:
                        pos_back += 1
                    cur_pos += 1
                leftflag = False
                
prefix = ""
if len(argv) > 2:
    prefix = argv[1]
    fn = argv[2]
else:
    fn = argv[1]

f = pysam.Samfile(fn, "rb")
depth_dic = {}
for cnt, ar in enumerate(f):
    if ar.tid == -1:
        continue
    chrom = f.getrname(ar.tid)
    if prev_chrom != chrom:
        if prev_chrom != "":
            fo.close()
        
        prev_chrom = chrom
        if prefix == "":
            fo = open(chrom+"_depth.txt", "w")
        else:
            fo = open(prefix+chrom+"_depth.txt", "w")
    pos = ar.pos+1
    cigar = ar.cigar
    
    if pos != prev_pos:
        if prev_pos != -1:
            process_chunk(linechunk)
            for i in range(prev_pos, pos):
                try:
                    fo.write('%s:%d\t%d\n'%(chrom, i, depth_dic[i]))
                    del depth_dic[i]
                except KeyError:
                    fo.write('%s:%d\t%d\n'%(chrom, i, 0))
        prev_pos = pos
        linechunk = [ (chrom, pos, cigar) ]
    else:
        linechunk.append( (chrom, pos, cigar) )
    if cnt % 50000 == 0:
        msg = "@"+chrom+": "+str(pos)
        sys.stdout.write(msg);sys.stdout.flush()
        sys.stdout.write("\b"*len(msg));sys.stdout.flush()
        

process_chunk(linechunk)
for i in range(pos, pos+150):
    try:
        fo.write('%s:%d\t%d\n'%(chrom, i, depth_dic[i]))
    except KeyError:
        fo.write('%s:%d\t%d\n'%(chrom, i, 0))

f.close()
fo.close()    
