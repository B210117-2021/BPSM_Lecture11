#!/usr/local/bin/python3
import subprocess

subprocess.call("grep -v '>' remote_gene_seq.fasta>remote_seq.fasta", shell=True)

a = open("remote_seq.fasta").read().upper()
b = open("plain_genomic_seq.txt").read().upper()
single_line_remote = a.replace("\n","")
single_line_local = b.replace("\n","")

#print(set(list(a)))
#print(set(list(b)))

single_line_local_left = single_line_local.replace("K","").replace("L","").replace("S","").replace("X","")

print(single_line_local_left)

remote_noncoding1 = single_line_remote[0:28]
remote_noncoding2 = single_line_remote[409:]
remote_coding = single_line_remote[29:408]

local_coding1 = single_line_local_left[0:62]
local_coding2 = single_line_local_left[90:]
local_noncoding = single_line_local_left[63:89]

remote_noncoding1_out = open("remote_noncoding1.fasta",'w')
remote_noncoding2_out = open("remote_noncoding2.fasta",'w')
remote_coding_out = open("remote_coding.fasta",'w')

remote_noncoding1_out.write(">AJ223353_noncoding1_length"+str(len(remote_noncoding1))+"\n")
remote_noncoding1_out.write(remote_noncoding1)
remote_noncoding1_out.close()


remote_noncoding2_out.write('>AJ223353_noncoding2_length'+str(len(remote_noncoding2))+"\n")
remote_noncoding2_out.write(remote_noncoding2)
remote_noncoding2_out.close()

remote_coding_out.write('>AJ223353_coding_length'+str(len(remote_coding))+"\n")
remote_coding_out.write(remote_coding)
remote_coding_out.close()


local_exon1_out = open("local_exon1.fasta",'w')
local_exon2_out = open("local_exon2.fasta",'w')
local_intron_out = open("local_intron.fasta",'w')

local_exon1_out.write('>local_exon1_length'+str(len(local_coding1))+"\n")
local_exon1_out.write(local_coding1)
local_exon1_out.close()

local_exon2_out.write('>local_exon2_length'+str(len(local_coding2))+"\n")
local_exon2_out.write(local_coding2)
local_exon2_out.close()

local_intron_out.write('>local_intron_length'+str(len(local_noncoding))+"\n")
local_intron_out.write(local_noncoding)
local_intron_out.close()


subprocess.call("sed '' remote_exon.fasta local_exon1.fasta local_exon2.fasta > merge_exon.fasta", shell = True)
subprocess.call("sed '' remote_intron1.fasta remote_intron2.fasta local_intron.fasta > merge_intron.fasta", shell = True)

