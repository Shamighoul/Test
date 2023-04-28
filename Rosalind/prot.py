from Bio import Seq

with open("rosalind_prot.txt", 'r' ) as inf, open("rosalind_out.txt", 'w') as wr:
    rna = inf.readline().strip()
    w = Seq.translate(rna) 
    print(w)
    wr.write(w)
