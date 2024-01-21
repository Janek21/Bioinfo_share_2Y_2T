from Bio import SeqIO

def ex8():
    fastq_file="/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/1-FastQ_parsing+Qcheck/1S-unknown_illumina_2024.fastq" #set path to fastq file
    f=open("/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/1-FastQ_parsing+Qcheck/OUTPUT.fasta", "w")#create new fasta file, with writing permission
    for read in SeqIO.parse(fastq_file, "fastq"):#read the fastq file, and for every read
        print(">"+str(read.id), file=f)#write > and the id
        print(read.seq, file=f)#write the sequence
    f.close()
    
print(ex8())


#bash that does the same as program
#cat 1S-unknown_illumina_2024.fastq | awk '{if(NR%4==1) {printf(">%s\n",substr($0,2));} else if(NR%4==2) print;}' > OUTPUT.fasta


#Get multiple sequences from file, upload to blastn one at a time, seek common organism (Podarcis lilfordi)
#download fasta sequence from the organism with lowest E-value as ref_seq.fasta (in my case i went to ncbi and got the whole genome), convert it into a database using:
#$ makeblastdb -in ref_seq.fasta -dbtype nucl -out reference_database
#blast our fasta sequence against the database to find the E-values
#$ blastn -query OUTPUT.fasta -db reference_database -out results.txt

#Use
'''
>A00500:270:H7YGVDSX2:1:1101:14705:1000 1:N:0:TAAGTATG
NGGCTCGCATCACAACCGGACAGCTAAACCAACTGCACTGTGAGAAATGCCAGCCCAGGCTACTTGTTTAACAGAATGGGGGCAGCTGAAATGCGCCCACAGTGAAGTTTAATGGAAGGGTGAGGAGACCCTGGCCCCGCAAGTTGCTCAG
>A00500:270:H7YGVDSX2:1:1101:22679:1000 1:N:0:AGGTACGC
GTGAAATCGCTAGTAGGTCCATATCTCCCCTCTGCCTGCCTCATTTTCCTCTCAGAAACAAAATATCCCCTCTCCCTGTGCTCCATTCACATAGAAAGAAAGGGTGGGTCCAGTTTTAAAATAAAAAGGGCATATGGCTAAGGAGCGAAGA
>A00500:270:H7YGVDSX2:1:1101:24957:1000 1:N:0:AGGTACGC
TTACTCATCAACGCTAAAAGGCAAAGTCTTGGGCGCTTTGGGAACAAACTGCGCCAGGCGATCAAGGAATAACCTCTACTCCAGGAAGCGTTTCCTCCCAATTCTGGACAGCTTGATAGAGCCAGAGCTTATCTATATGTGTACACTATAA
'''