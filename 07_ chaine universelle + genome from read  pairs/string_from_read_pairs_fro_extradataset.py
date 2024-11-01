
"""
unlike previous string reconstruction from a small dataset, Here I encounter a
RecursionError because the DFS implementation is hitting Python's recursion limit with this bigger dataset.
happens with recursive DFS on large graphs. So I modify the find_eulerian_path
function to use an iterative approach instead of recursion (dfs).

mais ça ne marche pas, je reste bloqué dans un cycle, relis duplicats...
"""

from parse_readpairs import parse_readpairs_file
paired_reads = parse_readpairs_file("extra_dataset_readpairs")

k, d = 50, 200

def prefix(kmer):
    """Get prefix of a k-mer by removing the last character
    Example: prefix('ACGT') returns 'ACG'"""
    return kmer[:-1]


def suffix(kmer):
    """Get suffix of a k-mer by removing the first character
    Example: suffix('ACGT') returns 'CGT'"""
    return kmer[1:]


# Functions to handle paired k-mers
def paired_prefix(paired_kmer):
    """Get the prefix of a paired k-mer by getting prefix of both parts
    Example: paired_prefix('GAGA|TTGA') returns 'GAG|TTG'

    Args:
        paired_kmer: String in format "left|right"
    Returns:
        String with prefix of left and right parts, separated by '|'
    """
    left, right = paired_kmer.split('|')  # Split at the '|' character
    return f"{prefix(left)}|{prefix(right)}"


def paired_suffix(paired_kmer):
    """Get the suffix of a paired k-mer by getting suffix of both parts
    Example: paired_suffix('GAGA|TTGA') returns 'AGA|TGA'

    Args:
        paired_kmer: String in format "left|right"
    Returns:
        String with suffix of left and right parts, separated by '|'
    """
    left, right = paired_kmer.split('|')
    return f"{suffix(left)}|{suffix(right)}"


def paired_debruijn_graph(paired_reads):
    """Create a de Bruijn graph from paired reads

    A de Bruijn graph represents overlaps between k-mers:
    - Nodes are (k-1)-mers (prefixes/suffixes of k-mers)
    - Edges represent k-mers connecting these nodes

    For paired reads, we maintain pairs at each step.

    Args:
        paired_reads: List of strings in format "left|right"
    Returns:
        Dictionary representing graph where:
        - Keys are prefix pairs
        - Values are lists of (suffix_pair, original_read) tuples
    """
    graph = {}
    for read in paired_reads:
        # Get prefix and suffix for current read
        pref = paired_prefix(read)
        suff = paired_suffix(read)

        # Add to graph: prefix -> [(suffix, original_read)]
        if pref not in graph:
            graph[pref] = []
        graph[pref].append((suff, read))
    return graph


def find_eulerian_path(graph):
    """Find an Eulerian path in the graph using iterative DFS

    Args:
        graph: Dictionary representing paired de Bruijn graph
    Returns:
        List of paired reads in correct order
    """
    # Count incoming edges for each node
    in_degrees = {}
    for node in graph:
        if node not in in_degrees:
            in_degrees[node] = 0
        # Count incoming edges to each neighbor
        for next_node, _ in graph[node]:
            if next_node not in in_degrees:
                in_degrees[next_node] = 0
            in_degrees[next_node] += 1

    # Find start node: should have one more outgoing than incoming edge
    start = next(iter(graph.keys()))  # Default to first node
    for node in graph:
        if len(graph.get(node, [])) > in_degrees.get(node, 0):
            start = node
            break

    # Iterative DFS using a stack
    path = []
    stack = [(start, None)]  # (current_node, edge_used)
    edges_used = set()  # Track used edges to avoid cycles

    while stack:
        current, edge = stack[-1]  # Peek at top of stack

        # If we used an edge to get here, add it to the path
        if edge is not None and edge not in edges_used:
            path.append(edge)
            edges_used.add(edge)

        # Find next unused edge from current node
        found_edge = False
        while graph.get(current, []):  # While current node has edges
            next_node, read = graph[current].pop()  # Get next edge
            edge_key = (current, next_node, read)  # Create unique edge identifier

            if edge_key not in edges_used:  # If edge hasn't been used
                stack.append((next_node, edge_key))  # Add to stack
                found_edge = True
                break

        if not found_edge:  # If no unused edges found, backtrack
            stack.pop()

    # Extract just the reads from the edge identifiers
    result = []
    for edge in path:
        _, _, read = edge
        result.append(read)

    return result


def string_reconstruction_from_readpairs(k, d, paired_reads):
    """Reconstruct string from paired reads

    Args:
        k: Length of each k-mer
        d: Distance between paired k-mers
        paired_reads: List of paired k-mer strings
    Returns:
        Reconstructed string
    """
    # Build graph and find path
    graph = paired_debruijn_graph(paired_reads)
    path = find_eulerian_path(graph)

    if not path:  # Check if path was found
        return None

    # Initialize patterns for both parts of the pairs
    first_pattern = []  # Will store left k-mers
    second_pattern = []  # Will store right k-mers

    # Process each read in path
    for read in path:
        left, right = read.split('|')
        # For first read, take whole k-mer
        if not first_pattern:
            first_pattern.extend(left)
        else:
            # For subsequent reads, just take last character
            first_pattern.append(left[-1])

        if not second_pattern:
            second_pattern.extend(right)
        else:
            second_pattern.append(right[-1])

    # Combine patterns with correct overlap
    k_plus_d = k + d
    result = ''.join(first_pattern)  # First pattern complete
    # Add second pattern starting after k+d positions
    result += ''.join(second_pattern[-(len(second_pattern) - k_plus_d):])

    return result

result = string_reconstruction_from_readpairs(k, d, paired_reads)
print(f"Reconstructed string: {result}")

#############################
########## TESTS ############
#############################

def read_expected_sequence(filename='attendu'):
    """Read the expected sequence from file

    Args:
        filename: Name of file containing expected sequence
    Returns:
        String containing expected sequence or None if error
    """
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None


def verify_identity(result, expected):
    """Verify perfect identity between sequences

    Args:
        result: Obtained sequence
        expected: Expected sequence
    """
    print("\n=== IDENTITY VERIFICATION ===")

    if not expected:
        print("Unable to verify - expected sequence not available")
        return

    # Compare lengths
    result_len = len(result)
    expected_len = len(expected)
    print(f"Obtained length:  {result_len}")
    print(f"Expected length: {expected_len}")

    if result_len != expected_len:
        print(f"❌ Sequences have different lengths")
        return

    # Verify identity
    if result == expected:
        print("✅ Sequences are IDENTICAL")
        return

    # If different, find first difference
    print("❌ Sequences are DIFFERENT")
    for i in range(result_len):
        if result[i] != expected[i]:
            print(f"\nFirst difference at position {i}:")
            start = max(0, i - 20)
            end = min(result_len, i + 20)

            print("\nObtained:")
            print(f"...{result[start:i]}[{result[i]}]{result[i + 1:end]}...")
            print("Expected:")
            print(f"...{expected[start:i]}[{expected[i]}]{expected[i + 1:end]}...")
            break

    # Write result to file for comparison
    with open('resultat_obtenu.txt', 'w') as f:
        f.write(result)
    print("\nThe obtained result has been written to 'resultat_obtenu.txt'")


def main():
    """Main function to run the string reconstruction with testing"""
    try:
        # Parse read pairs
        paired_reads = parse_readpairs_file("extra_dataset_readpairs")
        print(f"Successfully parsed {len(paired_reads)} valid paired reads")
        print(f"Example paired read: {paired_reads[0]}")
        print(f"k-mer length (k): {k}")

        # Read expected sequence
        expected_sequence = read_expected_sequence()

        # Get result
        result = string_reconstruction_from_readpairs(k, d, paired_reads)

        # Verify identity
        if result:
            verify_identity(result, expected_sequence)
        else:
            print("Error: Failed to reconstruct sequence")

    except Exception as e:
        print(f"Error during execution: {str(e)}")


if __name__ == "__main__":
    main()