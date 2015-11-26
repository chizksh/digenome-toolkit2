import string
from sys import argv

def load_forward( file_name  ):
    for_list = []
    f =open(file_name+'.txt')
    
    for line in f.xreadlines():
        units = line.split()
        for_list.append( [ string.atoi(units[0]), string.atoi(units[1]), string.atof(units[3]) ] )
    f.close()
    
    return for_list
 
def load_reverse( file_name ):
    rev_list = []
    f =open(file_name+'.txt')
    
    for line in f.xreadlines():
        units = line.split()
        rev_list.append( [ string.atoi( units[0] ), string.atoi( units[1] ), string.atof( units[3] ) ] )
    f.close()
    
    return rev_list

def for_to_rev(i, forward_file ,reverse_file):
    
    score_dict1 = {}
    score_dict2 = {}
    counter = 0
    j = 0
    score_dict = score_dict1
    rev_list=[]

    
    rev_list=load_reverse(reverse_file)
    
    f= open(forward_file+'.txt')
    for line in f.xreadlines():
        counter+=1
        units = line.split()
        for_seq = string.atoi( units[0] )
        for_count = string.atoi( units[1] )
        for_percent = string.atof( units[3] )
 
        try:
            score_dict[for_seq] = 0
        except MemoryError:
            score_dict= score_dict2
            score_dict[for_seq] = 0
        
        
        
        
        while j < len(rev_list):
            rev_seq = rev_list[j][0]
            rev_count = rev_list[j][1]
            rev_percent = rev_list[j][2]

            if (for_seq == rev_seq-1 or
                for_seq == rev_seq+0 or
                for_seq == rev_seq+1 or
                for_seq == rev_seq+2 or
                for_seq == rev_seq+3):
                
                score = for_percent * rev_percent * ((for_count)+(rev_count))
                score_dict[for_seq] = score_dict.get(for_seq) + score

            j += 1
            
            if for_seq+4 < rev_seq:
                j = max(0, j-10)
                break
                
      
    
    export_to_file( [score_dict1, score_dict2],forward_file)
                
def rev_to_for(i, forward_file, reverse_file ):
    
    score_dict1 = {}
    score_dict2 = {}
    counter = 0
    j = 0
    score_dict = score_dict1
    for_list = []

    for_list = load_forward(forward_file)
    
    f= open(reverse_file+'.txt')
    for line in f.xreadlines():
        counter+=1
        units = line.split()
        rev_seq = string.atoi( units[0] )
        rev_count = string.atoi( units[1] )
        rev_percent = string.atof( units[3] )
        
        
        try:
            score_dict[rev_seq] = 0
        except MemoryError:
            score_dict= score_dict2
            score_dict[rev_seq] = 0
            
        
            
        while j < len(for_list):
            for_seq = for_list[j][0]
            for_count = for_list[j][1]
            for_percent = for_list[j][2]

            if (rev_seq == for_seq-1 or
                rev_seq == for_seq+0 or
                rev_seq == for_seq+1 or
                rev_seq == for_seq+2 or
                rev_seq == for_seq+3):
                
                score = rev_percent * for_percent * ((for_count)+(rev_count))
                score_dict[rev_seq] = score_dict.get(rev_seq) + score

            j += 1
            
            if rev_seq+4 < for_seq:
                j = max(0, j-10)
                break
    
    export_to_file([score_dict1, score_dict2],reverse_file)
    
def export_to_file(dict_ary, header):
    #print drt+" export_to_file processing...",
    f = open( header+"_digenome_score.txt" , 'w')
    for dic in dict_ary:
        keys = dic.keys()
        keys.sort()
        for key in keys:
            if dic[key]!=0:f.write( str(key)+" "+str(dic[key])+'\n')
    f.close()        
    #print " done."


argvs = '\t'.join(argv)
#print argvs
ffn = argv[1]
rfn = argv[2]
chrom = argv[3]
try:
    pre_prefix = argv[4]
except:
    pre_prefix=""
    pass

ffnheader = '.'.join(ffn.split('.')[:-1])
rfnheader = '.'.join(rfn.split('.')[:-1])

msg = 'Digenome Scoring {0}{1}...'.format(pre_prefix, chrom)
sys.stdout.write(msg);sys.stdout.flush()
sys.stdout.write("\b"*len(msg));sys.stdout.flush()    
#ff = open(ffn); rf = open(rfn)

rev_to_for(chrom,ffnheader,rfnheader)
for_to_rev(chrom,ffnheader,rfnheader)
sys.stdout.write(" "*len(msg));sys.stdout.flush()
sys.stdout.write("\b"*len(msg));sys.stdout.flush()

#ff.close();rf.close()


