## Minghao Guo
## usage python extract_lenth.py -i your_fasta_file.fasta
## get the chromosomes length in a fasta file

import argparse
from Bio import SeqIO

def extract_chromosome_lengths(fasta_file):
    # Parse the FASTA file using SeqIO
    records = list(SeqIO.parse(fasta_file, 'fasta'))
    
    # Create a list of tuples with sequence headers and their respective lengths
    chromosome_lengths = [(record.id, len(record.seq)) for record in records]
    
    return chromosome_lengths

def main():
    parser = argparse.ArgumentParser(description="Extract chromosome names and lengths from a FASTA file.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input FASTA file.")
    
    args = parser.parse_args()

    results = extract_chromosome_lengths(args.input)

    # Get the filename without extension
    output_filename = args.input.split(".")[0] + "_chr_length.txt"

    with open(output_filename, 'w') as output_file:
        for name, length in results:
            output_file.write(f"{name}: {length} bp\n")

    print(f"Results written to {output_filename}")

if __name__ == "__main__":
    main()
