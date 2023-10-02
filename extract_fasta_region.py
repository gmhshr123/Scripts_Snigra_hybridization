## Minghao Guo
## Usage:  python extract_fasta_region.py -i your_fasta_file.fasta -id sequence_ID_you_want -s start_position -e end_position -o output.fasta



import argparse
from Bio import SeqIO

def extract_region_from_fasta(input_file, sequence_id, start, end, output_file):
    with open(input_file, 'r') as fasta_file, open(output_file, 'w') as output:
        for record in SeqIO.parse(fasta_file, 'fasta'):
            if record.id == sequence_id:
                extracted_sequence = record.seq[start-1:end]  # python uses 0-based indexing
                extracted_record = SeqIO.SeqRecord(extracted_sequence, id=record.id, description=f"extracted: {start}-{end}")
                SeqIO.write(extracted_record, output, 'fasta')
                break
        else:
            print(f"Sequence with ID {sequence_id} not found in the file.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract a specific region from a FASTA file")
    parser.add_argument('-i', '--input', required=True, help="Path to the input FASTA file")
    parser.add_argument('-id', '--sequence_id', required=True, help="ID of the sequence from which to extract")
    parser.add_argument('-s', '--start', type=int, required=True, help="Start position of the region to extract (1-based)")
    parser.add_argument('-e', '--end', type=int, required=True, help="End position of the region to extract (1-based)")
    parser.add_argument('-o', '--output', required=True, help="Path to the output FASTA file")

    args = parser.parse_args()
    extract_region_from_fasta(args.input, args.sequence_id, args.start, args.end, args.output)

