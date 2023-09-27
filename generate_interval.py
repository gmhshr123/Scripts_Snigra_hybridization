import argparse
from Bio import SeqIO
import csv

def generate_intervals(fasta_file, interval_size=1000000):
    """
    Generates intervals of specified length for each chromosome/scaffold in the FASTA file.
    """
    intervals = []

    # Parse the FASTA file using SeqIO
    with open(fasta_file, 'r') as f:
        seq_records = SeqIO.to_dict(SeqIO.parse(f, 'fasta'))

    for chrom, sequence in seq_records.items():
        end = len(sequence.seq)
        i = 1
        j = interval_size
        if end < j:
            intervals.append((chrom, i, end))
        else:
            while end > j:
                intervals.append((chrom, i, j))
                if end > j + interval_size:
                    i = j + 1
                    j = j + interval_size
                else:
                    i = j + 1
                    intervals.append((chrom, i, end))
                    break

    return intervals

def main():
    parser = argparse.ArgumentParser(description="Generate intervals of 1000,000 bp across all chromosomes and scaffolds from a FASTA file.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input FASTA file.")
    
    args = parser.parse_args()

    intervals = generate_intervals(args.input)

    # Define the output file name based on the input FASTA file name
    output_filename = args.input.split(".")[0] + "_intervals.txt"

    with open(output_filename, 'w', newline='') as outputFile:
        writer = csv.writer(outputFile, delimiter='\t')
        for interval in intervals:
            writer.writerow(interval)

    print(f"Intervals written to {output_filename}")

if __name__ == "__main__":
    main()
