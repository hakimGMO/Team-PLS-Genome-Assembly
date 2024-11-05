
# inputs rosalind
k, d = 4, 2
paired_reads = [
    "GAGA|TTGA",
    "TCGT|GATG",
    "CGTG|ATGT",
    "TGGT|TGAG",
    "GTGA|TGTT",
    "GTGG|GTGA",
    "TGAG|GTTG",
    "GGTC|GAGA",
    "GTCG|AGAT"
]



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
    """Find an Eulerian path in the graph using DFS (Depth-First Search)

    An Eulerian path visits every edge exactly once.
    Steps:
    1. Find start node (node with out_degree > in_degree)
    2. Use DFS to find path
    3. Reverse path (because DFS builds it backwards)

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

    # Use DFS to find path
    path = []

    def dfs(node):
        """Recursive DFS function
        Explores graph deeply before backtracking
        Adds reads to path as it backtracks"""
        while graph.get(node, []):  # While node has unused edges
            next_node, read = graph[node].pop()  # Remove and get next edge
            dfs(next_node)  # Recursively process next node
            path.append(read)  # Add read to path (during backtrack)

    dfs(start)  # Start DFS from chosen start node
    return path[::-1]  # Reverse path to get correct order


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


# les tests intermediaires


# Test 1: View the paired graph structure
print("\n=== STEPS ===")
print("\n1. Graph Structure:")
graph = paired_debruijn_graph(paired_reads)
for node, edges in graph.items():
    for edge in edges:
        print(f"{node} → {edge[0]} ({edge[1]})")

# Test 2: Show the path of reads
print("\n2. Path through graph:")
path = find_eulerian_path(graph)
for i, read in enumerate(path, 1):
    print(f"Step {i}: {read}")

# Test 3: Show overlaps between consecutive reads
print("\n3. Overlaps between reads:")
for i in range(len(path) - 1):
    current = path[i]
    next_read = path[i + 1]

    # Get the overlap
    current_suffix = paired_suffix(current)
    next_prefix = paired_prefix(next_read)

    print(f"\nReads {i + 1} and {i + 2}:")
    print(f"Current: {current}")
    print(f"Next:    {next_read}")
    print(f"Overlap: {current_suffix} = {next_prefix}")

# Test 4: Final result verification
print(f"\n4. Final String: {result}")
print("\nVerifying paired reads (k={k}, d={d}, k+d={k+d}):")
for read in paired_reads:
    left, right = read.split('|')
    left_pos = result.find(left)
    if left_pos != -1:
        right_pos = result.find(right)
        dist = right_pos - left_pos
        status = "✓" if dist == k + d else "✗"
        print(f"{status} {read}: distance = {dist}")
    else:
        print(f"✗ {read}: not found")