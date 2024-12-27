import time
from collections import defaultdict
from itertools import combinations
import networkx as nx

def parse_input(data):
    graph = defaultdict(set)
    for line in data:
        left = line[0:2]
        right = line[3:5]
        # print(left,right)
        graph[left].add(right)
        graph[right].add(left)
    # print(graph)
    return graph


def part1(graph):
    valid_sets = set()
    for key in graph.keys():
        if key[0] != 't':
            continue
        value_combinations = list(combinations(graph[key], 2))
        for elem1, elem2 in value_combinations:
            if elem2 in graph[elem1]:
                valid_sets.add(tuple(sorted([key, elem1, elem2])))
    # print(valid_sets)
    return len(valid_sets)

def part2(graph):
    G = nx.Graph()
    for node in graph.keys():
        neighbors = graph[node]
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Find the largest clique
    largest_clique = max(nx.find_cliques(G), key=len)

    # print("Maximum Clique:", largest_clique)
    # print("Size of Maximum Clique:", len(largest_clique))
    return ",".join(sorted(largest_clique))


if __name__=="__main__":
    print("\n--- Day 23: LAN Party ---")
    file = open("advent_of_code_2024/day23_input.txt","r")
    data = [x.strip() for x in file.readlines()]
    # parse_input(data)
    graph = parse_input(data)
    # print(data)

    print("Part 1:")
    start1 = time.time()
    print(part1(graph))
    end1 = time.time()
    print(f"Elapsed time: {end1-start1:.4f} seconds")

    print("Part 2:")
    start2 = time.time()
    print(part2(graph))
    end2 = time.time()
    print(f"Elapsed time: {end2-start2:.4f} seconds")
    print()