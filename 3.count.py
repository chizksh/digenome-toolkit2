from sys import argv
from collections import defaultdict
import sys
try:	
	range_sum = 0
	fns = []
	for i in range(1, len(argv)):
	    if i != len(argv)-1 and argv[i] == "-u":
	        range_sum = int(argv[i+1])
	    elif i != 0 and argv[i-1] != "-u":
	        fns.append(argv[i])
	
	bufs = defaultdict(lambda: 0)
	for fn in fns:
	    
	    fnhead = '.'.join(fn.split('.')[:-1])
	    f = open(fn)
	    msg = 'count %s...'%(fn.strip('./'))
	    sys.stdout.write(msg);sys.stdout.flush()
	    sys.stdout.write("\b"*len(msg));sys.stdout.flush()
	    
	    prev = ""
	    cnt = 0
	    for line in f:
	        line = line.strip()
	        if line != prev:
	            if cnt != 0:
	                pos = int(prev)
	                for i in range(max(1, pos-range_sum), pos+range_sum+1):
	                    bufs[i] += cnt
	            prev = line
	            cnt = 0
	        cnt += 1
	    f.close()
	
	    pos = int(prev)
	    for i in range(max(1, pos-range_sum), pos+range_sum+1):
	        bufs[i] += cnt
	
	    l = list(bufs.items())
	    l.sort(key=lambda e:e[0])
	    with open(fnhead + '_freq.txt', 'w') as fo:
	        for key, val in l:
	            fo.write("%d\t%d\n"%(key, val))
	    sys.stdout.write(" "*len(msg));sys.stdout.flush()
	    sys.stdout.write("\b"*len(msg));sys.stdout.flush()
except IOError:
	print fn+":File can't be opened"
	pass
except Exception as e:
	print e
	pass
    
