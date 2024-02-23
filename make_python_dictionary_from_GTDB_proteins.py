#!/usr/bin/env python

# Julian Damashek, Hamilton College
# jdamashe@hamilton.edu, juliandamashek@gmail.com

# Takes a file with names of contigs from all the GTDB genomes (usually split archaea and bacteria separately)
#		and makes a python dictionary to link the GTDB and NCBI accessions.
# That file came from running (with archaea.txt and bacteria.txt being lists of accession numbers): 
#		for i in `cat archaea.txt`; do echo $i && gunzip -c ${i}.?_protein.faa.gz | grep ">"; done | cut -d'.' -f1 | awk '! a[$0]++' > archaea_gtdb_ncbi_for_dict.txt
#		or,
#		for i in `cat bacteria.txt`; do echo $i && gunzip -c ${i}.?_protein.faa.gz | grep ">"; done | cut -d'.' -f1 | awk '! a[$0]++' > bacteria_gtdb_ncbi_for_dict.txt

# Note, this is written in python2 (2.7.16 was the last test) and not yet updated to python3. One day...

# Usage: make_python_dictionary_from_GTDB_proteins.py [file from above as *for_dict.txt]

import sys
import csv
import ast
import collections
import re

#save dictionary
with open(str(sys.argv[1]), 'r') as in_file:
	with open(str(sys.argv[1].split('for_dict.txt')[0]+'dict.txt'),'w') as out_file:
		GTDB_name = 'blank' #to save GTDB names during iteration
		NCBI_name = 'blank'
		out_file.write('{')
		
		for line in in_file:
			if not line.startswith('>'): 
				GTDB_name = line.strip('\r\n')
			else:
				seq_name = line.strip('\r\n').split('>')[1].split('.')[0]
				if seq_name != NCBI_name:
					NCBI_name = seq_name
					out_file.write('\n'+'\''+str(NCBI_name)+'\':\''+str(GTDB_name)+'\',')
		out_file.write('}')

print("Hard work done! Go look things up in your fancy new dictionary!")
			