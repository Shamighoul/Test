from Bio import SeqIO
from string import *

with open("rosalind_revc.txt", 'r' ) as inf, open("rosalind_out.txt", 'w') as w:
    d = inf.readline().upper()
    d=d[ : :-1]
#     print(''.join(d.replace('A', 'z').replace('T',
#                                               'A').replace('z', 'T').replace('C', 'x').replace('G', 'C').replace('x', 'G')))
    w.write(''.join(d.replace('A', 'z').replace('T',
                                               'A').replace('z', 'T').replace('C', 'x').replace('G', 'C').replace('x', 'G')))
