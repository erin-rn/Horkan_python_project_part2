#!/usr/bin/env python
# coding: utf-8

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import Phylo
from Bio import SeqIO

records = SeqIO.parse('sequence.gb',"gb")
Accession = []
Family = []
Genus = []
Species = []
Num_Features = []
Source = []

for record in records:
        Accession.append(record.id)
        Family.append(record.annotations['taxonomy'][-2])
        Genus.append(record.annotations['organism'].split(' ')[0])
        Species.append(record.annotations['organism'].split(' ')[1])
        Num_Features.append(len(record.features))
        Source.append(record.annotations['organism'])
d = { 'Accession': Accession , 'Family': Family , 'Genus': Genus , 'Species': Species , 'Num_Features': Num_Features , 'Source': Source}
import pandas as pd
df = pd.DataFrame(d)
df.to_csv('genbank_parse.csv')

