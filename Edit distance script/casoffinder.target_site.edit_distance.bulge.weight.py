import Levenshtein as l

target_f = open('./Target sites.txt','r')
target_dic ={}

for line in target_f.xreadlines():
    units = line.split()
    gene=units[0]
    seq=units[1]
    target_dic[gene] = seq

for each in target_dic.keys():
    each_file = './' + each + '.txt'
    each_f = open (each_file, 'r')
    each_out = open ('./result_'+each+'.txt','w')
    header = each_f.readline()
    each_out.write(header.strip('\n')+'\t'+'bulge:1'+'\t'+'3'+'\t'+'5'+'\n')
    for line in each_f.xreadlines():
        units = line.split()
        target_seq = units[4]
        value ={}
        for nuc in "ATGC":
            target_seq.replace('N',nuc)
            value[nuc] = (l.distance(target_seq,target_dic[each]),l.editops(target_seq,target_dic[each]))
        max_dist, max_editops = value[max(value, key=value.get)]
        step = []
        for each_editop in max_editops:
            a,b,c = each_editop
            step.append(a)
        deletion = step.count('delete')

        each_out.write(line.strip()+'\t'+str(max_dist)+'\t'+str(max_dist+deletion*2)+'\t'+str(max_dist+deletion*4)+'\n')
    each_f.close()
    each_out.close()
        
