from Bio import SeqIO

def ex8():
    fastq_file="/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/1-FastQ_parsing+Qcheck/1S-unknown_illumina_2024.fastq"
    f=open("/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/1-FastQ_parsing+Qcheck/Sequence.fasta", "w")
    for read in SeqIO.parse(fastq_file, "fastq"):
        print(">"+str(read.id), file=f)
        print(read.seq, file=f)
    f.close()
    
print(ex8())

#blastn -query OUTPUT.fasta -db nt -out result.txt -evalue 0.001 -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore"
#blastp -query “query_file”.fa -db “database”.fasta -out “name_output_file”.txt
#blastp -query  Sequence.fasta -out results.txt
#download nuclotide datbase, error en descarrega, time out,ns pq, demanar database a algu

#bash that does the same as program
#cat 1S-unknown_illumina_2024.fastq | awk '{if(NR%4==1) {printf(">%s\n",substr($0,2));} else if(NR%4==2) print;}' > OUTPUT.fast