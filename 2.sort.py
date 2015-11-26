from sys import argv # all reverse should be sorted
import sys
for arg in argv[1:]:
    with open(arg) as f:
        l = [int(line) for line in f]
    fns = arg.split(".")
    
    msg = "sort %s..."%(fns[-2].strip('/'))
    sys.stdout.write(msg);sys.stdout.flush()
    sys.stdout.write("\b"*len(msg));sys.stdout.flush()
    l.sort()
    
    with open('.'.join(fns[:-1]) + "_sorted.txt", 'w') as fo:
        fo.write('\n'.join(map(str, l)))
    