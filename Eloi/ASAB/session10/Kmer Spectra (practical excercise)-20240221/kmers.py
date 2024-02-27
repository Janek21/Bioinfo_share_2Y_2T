import sys
import matplotlib.pyplot as plt
from Bio import SeqIO

def clean_sequence(sequence):
    # Remove lowercase characters and convert 'n' to 'N'
    cleaned_sequence = ''.join(char.upper() if char.upper() in {'A', 'T', 'C', 'G'} else '' for char in sequence)
    
    return cleaned_sequence

def kmers_spectra(filename, k):
    # Read sequence file using SeqIO
    sequences = []
    with open(filename, 'r') as file:
        for record in SeqIO.parse(file, 'fastq' if 'fastq' in filename.lower() else 'fasta'):
            sequences.append(clean_sequence(record.seq))

    # Combine sequences into a single sequence
    seq = ''.join(sequences)

    # Count k-mers and their frequencies
    freq_d = {}
    for pos in range(len(seq)-k+1):
        kmer = seq[pos:pos+k]
        freq_d[kmer] = freq_d.get(kmer, 0) + 1

    # Count multiplicities
    mult_d = {}
    for freq in freq_d.values():
        mult_d[freq] = mult_d.get(freq, 0) + 1

    # Plotting
    keys, values = zip(*mult_d.items())
    plt.figure(figsize=(10, 6))
    plt.scatter(keys, values, color='skyblue', edgecolors='black', alpha=0.7, s=25)
    plt.title(f'K-mer Multiplicity Spectrum (k={k})', fontsize=16)
    plt.xlabel('Multiplicity', fontsize=14)
    plt.ylabel('Number of K-mers', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)

    # Save plot in the working directory with a dynamic filename
    plot_filename = f'kmer_spectrum_{(filename)}_k:{k}.png'
    plt.savefig(plot_filename)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python kmer_analysis.py <filename> <k>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        k = int(sys.argv[2])
    except ValueError:
        print("Error: k must be an integer.")
        sys.exit(1)

    kmers_spectra(filename, k)
