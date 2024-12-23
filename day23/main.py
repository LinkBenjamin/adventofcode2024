from collections import defaultdict
from itertools import combinations

def load(filename):
    data = []
    with open(filename) as f:
        raw = f.read().strip().split()
        for n in raw:
            data.append(n.strip().split('-'))
    return data

def is_clique(nodes):
    return all(v in graph[u] for u,v in combinations(nodes, 2))


# Borrowed this from https://github.com/Lkeurentjes/Advent_of_code/blob/64f09d591ea6d23ee687b050f19e162d56b2c80c/2024/2024-23-LAN_Party/2024-23-LAN_Party.py#L31 after getting an iterative version working, but unable to process large data sets.  I never took any graph theory type classes and this was a good learning experience.
def find_largest_clique(graph):
    # Bron–Kerbosch as helper algorithm
    def bron_kerbosch(current, candidates, processed, cliques):
        # Base case: No more candidates or processed vertices, meaning `current` is a maximal clique
        if not candidates and not processed:
            cliques.append(current)  # Add the maximal clique to the results
            return

        # Iterate through a copy of candidates (to modify the original set)
        for v in list(candidates):
            # Recursively build cliques including vertex v
            bron_kerbosch(
                current.union({v}),  # Add v to the current clique
                candidates.intersection(graph[v]),  # Filter candidates to v's neighbors
                processed.intersection(graph[v]),  # Filter processed to v's neighbors
                cliques  # Pass the cliques list for results
            )
            # Move vertex v from candidates to processed after exploring
            candidates.remove(v)
            processed.add(v)

    cliques = []
    bron_kerbosch(set(), set(graph.keys()), set(), cliques)
    largest_clique = max(cliques, key=len)

    return largest_clique

def generate_password(clique):
    # make output for part 2
    return ','.join(sorted(clique))

if __name__ == '__main__':
    data = load('data.txt')
    
    graph = defaultdict(set)
    for u, v in data:
        graph[u].add(v)
        graph[v].add(u)

    counter = 0
    triads = set()
    for node in graph:
        for neighbor in graph[node]:
            common = graph[node] & graph[neighbor]
            for connected_node in common:
                triad = tuple(sorted([node, neighbor, connected_node]))
                triads.add(triad)

    counter = sum(1 for triad in triads if any(node.startswith('t') for node in triad))
                    
    print(f"Triads: {triads}")
    print(f"Triads starting with t: {counter}")


    graph = {}
    for u,v in data:
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()
        graph[u].add(v)
        graph[v].add(u)
    
    clique = find_largest_clique(graph)

    print(generate_password(clique))