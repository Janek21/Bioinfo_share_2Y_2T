from Bio import SeqIO
import matplotlib.pyplot as plt

fastq_file="/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/1-FastQ_parsing+Qcheck/1S-unknown_illumina_2024.fastq"


def first_read_len(fastq_file):#Question 1,2,4

    for read in SeqIO.parse(fastq_file, "fastq"):
        print(read)

        quality=(read.letter_annotations['phred_quality'])
        print()
        print("Quality of the first read:")
        print(quality)
        print()
        return f"Length of the first read: {len(read.seq)}"
    

def reads_in_file(fastq_file):#Question 3

    c=0
    for read in SeqIO.parse(fastq_file, "fastq"):
        c+=1
    return f"There are {c} reads in the file"

def mean_of_quality(fastq_file):#Question 5, part 1

    q_list=[]
    for read in SeqIO.parse(fastq_file, "fastq"):
        q_list.append(read.letter_annotations['phred_quality'])
    #sublists are reads
    
    #total_means=np.mean(q_list, axis=0) #same as double for loop VV
    total_means=[]
    for i in range(len(q_list[0])):#add first(2nd, nth) element of every read divided by number of reads(mean) to local_mean
        local_mean=0
        for j in range(len(q_list)):
            local_mean+=int(q_list[j][i])/len(q_list)
        total_means.append(local_mean)#total is a list of means for position (total[0] is mean of 1st position of all reads)
    return total_means

def mean_quality_plot(fastq_file):#Question 5, part 2

    total_means=mean_of_quality(fastq_file)
    plt.plot(range(1, len(total_means)+1), total_means)
    plt.xlabel("Position in read")
    plt.ylabel("Mean quality score")
    plt.title("Read position Vs Quality")
    plt.show()

def error_prob(fastq_file): #Question 7
    total_means=mean_of_quality(fastq_file)
    error_means=[]
    for q in total_means:
        error_means.append(10**(-q/10))
    plt.plot(range(1, len(error_means)+1), error_means)
    plt.xlabel("Position in read")
    plt.ylabel("Mean quality score")
    plt.title("Read position Vs Quality")
    plt.show()
    return (max(error_means))
        
#print(first_read_len(fastq_file))
print()
#sprint(reads_in_file(fastq_file))
print(mean_quality_plot(fastq_file))
print(error_prob(fastq_file))