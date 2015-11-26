from sys import argv # [-p prefix], [-d direction], 1_freq, 1_depth, 2_freq, 2_depth, ...
from os.path import isfile
import sys

prefix = ""
direction = ""

fns = []
for i in range(1, len(argv)):
    if i != len(argv)-1 and argv[i] == "-p":
        prefix = argv[i+1]
    elif i != len(argv)-1 and argv[i] == "-d":
        direction = argv[i+1]
    elif i != 0 and argv[i-1] != "-p" and argv[i-1] != "-d":
        fns.append(argv[i])

if direction != "":
    fns = zip(fns[::2], fns[1::2])
    if prefix == "":
        fo = open("%s.txt"%direction, "a")
    else:
        fo = open("%s_%s.txt"%(prefix, direction), "a")

    firstline = True
    for ffn, fdn in fns:
        
        ff = open(ffn)
        fd = open(fdn)
        msg = "get_depth from {0} and {1}...".format(ffn.strip("./"), fdn.strip("./"))
        sys.stdout.write(msg);sys.stdout.flush()
        sys.stdout.write("\b"*len(msg));sys.stdout.flush()
        for ff_line in ff:
            pos = ff_line.split('\t')[0]
            while True:
                fd_line = fd.readline()
                try:
                    fd_pos = fd_line.split('\t')[0].split(':')[1]
                    while int(fd_pos) > int(pos):
                        ff_line = ff.readline()
                        pos = ff_line.split('\t')[0]
                    if fd_pos == pos:
                        if firstline:
                            firstline = False
                        else:
                            fo.write('\n')
                        fo.write(fd_line.strip())
                        break
                except:
                    #print (ff_line, fd_line)
                    break
        ff.close()
        sys.stdout.write(" "*len(msg));sys.stdout.flush()
        sys.stdout.write("\b"*len(msg));sys.stdout.flush()
    fo.write("\n")
