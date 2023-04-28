from Bio import SeqIO
from Bio.SeqUtils import GC
import numpy

dict = {}
g = {}
with open("rosalind_gc.txt", 'r' ) as inf, open("rosalind_out.txt", 'w') as wr:
    q = inf.readlines()
    i=-1
    while i<len(q):
        if q[i][0]=='>':
            w = i
            dict[q[w][1:].strip()] = ''
            i+=1
            while i<len(q) and q[i][0]!='>':
                dict[q[w][1:].strip()] += q[i].strip()
                i+=1
        else:
            i+=1
        
    for i in dict.keys():
        dict[i] = GC(dict[i])
    MX = max(dict.values())
    for i in dict.keys():
        if dict[i]==MX:
            ans = i
    print(ans+ '\n' + str(MX))
    wr.write(ans + '\n' + str(MX))
