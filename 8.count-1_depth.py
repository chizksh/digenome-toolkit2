import string
from sys import argv

for fn in argv[1:]:
    
    f = open(fn)
    msg = "count-1 depth {}".format(fn.strip('./'))
    sys.stdout.write(msg);sys.stdout.flush()
    sys.stdout.write("\b"*len(msg));sys.stdout.flush()
    fnhead = '.'.join(fn.split('.')[:-1])
    fo = open('{}_count-1.txt'.format(fnhead), 'w')
    for line in f.xreadlines():
        units = line.split()
        seq = units[0]
        count = string.atoi(units[1])
        depth = string.atoi(units[2])
        count_1_depth = (count-1)*1.0/depth
        if count-1 != 0 :
            s =  ( seq +" "+ str(count-1) +" "+ str(depth) +" "+ str(count_1_depth*100)+"\n" )
            fo.write(s)

    f.close();fo.close()
    sys.stdout.write(" "*len(msg));sys.stdout.flush()
    sys.stdout.write("\b"*len(msg));sys.stdout.flush()
    