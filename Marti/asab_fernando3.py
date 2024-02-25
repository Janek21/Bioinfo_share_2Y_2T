import matplotlib.pyplot as plt
import collections
from Bio import SeqIO

# Ex.1 
def kmer(seq, k):
	kmers = []
	equation = len(seq) - k + 1
	for i in range(equation):
		kmer = seq[i:i+k]
		kmers.append(kmer)
	return kmers

# Ex.2
def kmer2(fasta_file, k):

	fasta_path = '/home/marti/Baixades/kmer/fasta/read.fasta'
	fasta_file = open(fasta_path, 'r')
	lines = fasta_file.readlines()
	sequence = lines[1].strip()
	kmers = []
	equation = len(sequence) - k + 1
	for i in range(equation):
		kmer = sequence[i:i+k]
		kmers.append(kmer)
	return kmers


# Ex.3
def kmer_spectrum(seq, k):

	kmer_spectrum = {}
	kmers = kmer(seq, k)
	for kmer_sequence in kmers:
		if kmer_sequence in kmer_spectrum:
			kmer_spectrum[kmer_sequence] += 1
		else:
			kmer_spectrum[kmer_sequence] = 1
	return kmer_spectrum


def read_fasta(fasta_file):	
	sequences = []
	for record in SeqIO.parse(fasta_file, "fasta"):
		sequence = str(record.seq).upper()
		sequences.append(sequence)
	return sequences
	
def plot_kmer_spectrum(kmer_spectrum, k):
    
	kmer_spectrum_list = list(kmer_spectrum.items())
	kmer_spectrum_list = sorted(kmer_spectrum_list, key=lambda x: x[1], reverse=True)
    
	counts = []
	frequency = {}
	
	for x in kmer_spectrum_list:
		counts.append(x[1])
	
	for count in set(counts):
		count_freq = 0
		for x in counts:
			if x == count:
				count_freq += 1
		frequency[count] = count_freq
	
	frequency_list = []
	for count in counts:
		frequency_list.append(frequency[count])
	
	plt.scatter(counts, frequency_list, marker='.', alpha=0.7)
	plt.xlabel('Counts')
	plt.ylabel('Frequency')
	plt.title(f'K-mer Spectrum of {k}-mers')
	plt.show()

if __name__ == '__main__':
	fasta_file = '/home/marti/Baixades/kmer/fasta/GCF_000240185.1_ASM24018v2_genomic.fasta'
	sequences = read_fasta(fasta_file)
	k = 8
	kmer_spectrum = kmer_spectrum(sequences[0], k)
    
	plot_kmer_spectrum(kmer_spectrum, k)
