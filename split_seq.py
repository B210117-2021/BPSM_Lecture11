#!/usr/local/bin/python3

import subprocess

subprocess.call("grep -v '>' remote_gene_seq.fasta>remote_seq.fasta", shell=True)

a = open("remote_seq.fasta").read().rstrip()

single_line = a.replace("\n","")

plain_seq = open("plain_genomic_seq.txt")
plain_seq_con = plain_seq.read()



