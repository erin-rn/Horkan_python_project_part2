#!/usr/bin/env python
# coding: utf-8

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import Phylo
from Bio import SeqIO

proteins = SeqIO.parse('sequence.fasta', 'fasta')

ID = []
First = []
Len = []
NumC = []

for record in proteins:
    ID.append(record.id)
    First.append(record.seq[0:9])
    Len.append(len(record.seq))
    NumC.append(record.seq.count('C'))

import pandas as pd
dprot = { 'ID': ID, 'First_10_AA' : First, 'Length' : Len, 'Number_Cs': NumC}
data = pd.DataFrame(dprot)
data.to_csv('protein_info.csv')
