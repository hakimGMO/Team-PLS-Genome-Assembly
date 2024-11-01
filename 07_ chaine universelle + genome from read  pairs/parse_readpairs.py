def parse_readpairs_file(filename):
    """
    Parse a file containing paired reads and return a list of paired reads.
    Each line in the file contains two sequences separated by '|'.

    Args:
        filename (str): Path to the file containing paired reads

    Returns:
        list: List of paired reads in format ["seq1|seq2", "seq3|seq4", ...]
    """
    paired_reads = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                # Strip whitespace and skip empty lines
                line = line.strip()
                if not line:
                    continue

                # Verify the format (should contain exactly one '|')
                if '|' not in line or line.count('|') > 1:
                    print(f"Skipping invalid line format: {line}")
                    continue

                # Split the line into left and right sequences
                left_seq, right_seq = line.split('|')

                # Remove any whitespace from sequences
                left_seq = left_seq.strip()
                right_seq = right_seq.strip()

                # Verify sequence lengths (should be 50 for both parts)
                if len(left_seq) != 50 or len(right_seq) != 50:
                    print(f"Skipping line with incorrect sequence length: {line}")
                    print(f"Lengths: left={len(left_seq)}, right={len(right_seq)}")
                    continue

                # Verify sequences contain only valid DNA characters
                valid_chars = set('ACGT')
                if not (set(left_seq).issubset(valid_chars) and set(right_seq).issubset(valid_chars)):
                    print(f"Skipping line with invalid characters: {line}")
                    continue

                # Add valid paired read to list
                paired_reads.append(f"{left_seq}|{right_seq}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

    # Print summary statistics
    print(f"Successfully parsed {len(paired_reads)} valid paired reads")
    if paired_reads:
        print(f"Example paired read: {paired_reads[0]}")
        k = len(paired_reads[0].split('|')[0])  # length of each sequence
        print(f"k-mer length (k): {k}")

    return paired_reads


# Example usage
if __name__ == "__main__":
    filename = "extra_dataset_readpairs"
    paired_reads = parse_readpairs_file(filename)

    if paired_reads:
        # You can now use these paired reads with the string reconstruction algorithm
        k = 50  # length of each sequence in the pair
        d = 200  # distance between pairs (you might need to adjust this value)

        # Uncomment the following lines when ready to run the reconstruction
        # result = string_reconstruction_from_readpairs(k, d, paired_reads)
        # print(f"Reconstructed string: {result}")