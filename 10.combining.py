from sys import argv
import string
import sys
def comb(fn, chrom,ffnheader,rfnheader,overhang,threshhold=0):

    try:
    
        f1 = open( ffnheader+".txt")
        f2 = open( rfnheader+".txt")
        
        f3 = open( fn+"_digenome-seq_result_"+str(chrom)+".txt" , 'w')
        
        d_f2 = {}
        for lines in f2.xreadlines():
            units = lines.split()
            d_f2[int(units[0])]=float(units[1])
    
        for lines in f1.xreadlines():
            units = lines.split()
            for_seq = string.atoi(units[0])
            for_score = string.atof(units[1])
            if d_f2.has_key(for_seq-overhang):
                if (for_score+d_f2[for_seq-1])>threshhold:
                    
                    f3.write( str(for_seq)+" "+str(for_score)+" "
                              +str(for_seq-overhang)+" "+str(d_f2[for_seq-overhang])+" "
                              +str(for_score+d_f2[for_seq-overhang])+'\n' )
        f1.close()
        f2.close()
        f3.close()
    except IOError:
        print "IOError"
        pass

argvs = '\n'.join(argv)
ffn = argv[1]
rfn = argv[2]
chrom = argv[3]
fn = argv[4].split('/')[-1]

try:
    pre_prefix = argv[5]
except:
    pre_prefix=""
    pass
    
overhang = int(argv[6])
    
    
ffnheader = '.'.join(ffn.split('.')[:-1])
rfnheader = '.'.join(rfn.split('.')[:-1])


msg = 'Combining {0}{1}...'.format(pre_prefix, chrom)
sys.stdout.write(msg);sys.stdout.flush()
sys.stdout.write("\b"*len(msg));sys.stdout.flush()
#ff = open(ffn); rf = open(rfn)

comb(fn, chrom,ffnheader,rfnheader,overhang)
sys.stdout.write(" "*len(msg));sys.stdout.flush()
sys.stdout.write("\b"*len(msg));sys.stdout.flush()

