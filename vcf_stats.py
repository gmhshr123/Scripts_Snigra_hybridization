## Minghao Guo
## Usage: python vcf_stats.py path_to_your_vcf_file.vcf chromosome_counts.txt 
## counts the variant numbers for each chromsomes


import argparse

def count_chromosomes(vcf_file):
    # Initialize dictionary to store counts
    chrom_counts = {f"Chr{i:02}": 0 for i in range(1, 20)}

    # Read the VCF file and update the counts
    with open(vcf_file, 'r') as f:
        for line in f:
            # Skip headers starting with ##
            if line.startswith("##"):
                continue

            # Extract chromosome name from the line
            chrom = line.split('\t')[0]

            # If chromosome is in our list, update the count
            if chrom in chrom_counts:
                chrom_counts[chrom] += 1

    return chrom_counts

def export_to_txt(chrom_counts, output_file):
    with open(output_file, 'w') as f:
        for chrom, count in chrom_counts.items():
            f.write(f"{chrom}\t{count}\n")

def main():
    parser = argparse.ArgumentParser(description='Process VCF file and count lines for chromosomes Chr01 to Chr19.')
    parser.add_argument('input_vcf', type=str, help='Path to the input VCF file.')
    parser.add_argument('output_txt', type=str, help='Path to the output text file.')

    args = parser.parse_args()

    counts = count_chromosomes(args.input_vcf)
    export_to_txt(counts, args.output_txt)
    print(f"Chromosome counts exported to {args.output_txt}")

if __name__ == "__main__":
    main()

