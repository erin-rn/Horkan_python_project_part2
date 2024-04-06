#!/usr/bin/env python


from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import Phylo
from Bio import SeqIO


rudii = SeqIO.parse('GCA_rudii.fna', 'fasta')

for record in rudii:
    print(type(record))
    seq = record.seq
    lseq = len(seq)
    numGC = seq.count('GC')
    fATG = seq.count('ATG')
    rATG = seq.reverse_complement().count('ATG')

drudii = { 'Length': lseq, 'GC_Content' : numGC, 'ATG_Forward' : fATG, 'ATG_Reverse': rATG}
data = pd.DataFrame(drudii)
data.to_csv('rudii.csv')
    



