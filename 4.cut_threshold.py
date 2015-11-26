from sys import argv
import sys
fr = 5

for fn in argv[1:]:
    msg = 'cut_threshold %s...'%(fn.strip('./'))
    sys.stdout.write(msg);sys.stdout.flush()
    sys.stdout.write("\b"*len(msg));sys.stdout.flush()
    
    f = open(fn)
    fnhead = '.'.join(fn.split('.')[:-1])
    fo = open('{}_from_{}.txt'.format(fnhead, fr), 'w')
    for line in f:
        entries = line.split('\t')
        cnt = int(entries[1])
        if fr <= cnt:
            fo.write(line)
    fo.close()
    f.close()
    
    sys.stdout.write(" "*len(msg));sys.stdout.flush()
    sys.stdout.write("\b"*len(msg));sys.stdout.flush()