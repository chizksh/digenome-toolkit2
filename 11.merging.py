from sys import argv

fn = argv[1].split('/')[-1]
chrom = argv[2]
try:
    pre_prefix = argv[3]
except:
    pre_prefix = ""
    pass

fo = open ("%s_digenome-seq_result.txt"%(fn.split('.')[-2]), 'a')
f = open (fn+"_digenome-seq_result_"+str(chrom)+".txt")
for line in f.xreadlines():
    fo.write(chrom+" "+line)
f.close()
fo.close()