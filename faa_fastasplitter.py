#!/usr/bin/env python2

# Julian Damashek, Hamilton College
# jdamashe@hamilton.edu, juliandamashek@gmail.com

Usage = """,
Julian Damashek, Hamilton College

Take a .faa (amino acid) fasta file and split it into smaller files of set length.

Currently requires python2 (2.7.16 last version tested...)

Usage:
  > faa_fastasplitter.py [number of reads per file wanted] [big input fasta file, must have .faa extension]
""",

import sys
from Bio import SeqIO

def batch_iterator(iterator, batch_size):
    """Returns lists of length batch_size.

    """
    entry = True  # Make sure we loop once
    while entry:
        batch = []
        while len(batch) < batch_size:
            try:
                entry = iterator.next()
            except StopIteration:
                entry = None
            if entry is None:
                # End of file
                break
            batch.append(entry)
        if batch:
            yield batch

if len(sys.argv)<2:
	print Usage	
else:
	nreads = int(sys.argv[1])
	ffile = sys.argv[2]

#print(nreads)

record_iter = SeqIO.parse(open(ffile),"fasta")
for i, batch in enumerate(batch_iterator(record_iter, nreads)):
    filename = ffile.split('.faa')[0] + "_%i.faa" % (i + 1)
    with open(filename, "w") as handle:
        count = SeqIO.write(batch, handle, "fasta")
    print("Wrote %i records to %s" % (count, filename))
