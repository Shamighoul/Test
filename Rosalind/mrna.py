from collections import Counter
countMat =  { 'G': 4, 'A': 4, 'V': 4, 'L': 6, 'I': 3, 'P': 4, 'F': 2, 'Y': 2, 
             'W': 1, 'S': 6, 'T': 4, 'C': 2, 'M': 1, 'N': 2, 'Q': 2, 'K': 2, 'R': 6, 'H': 2, 'D': 2, 'E': 2, 'B': 4, 'Z': 4 }
ans = 3
with open("rosalind_mrna.txt", 'r' ) as inf, open("rosalind_out.txt", 'w') as wr:
    prot = inf.readline().strip()
    protmap = Counter(prot)        
    for elem in prot:
        ans*=countMat[elem]
        ans%=10**6
    wr.write(f'{ans}')
    print(ans)
