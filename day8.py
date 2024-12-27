from collections import defaultdict

def part1(map_grid):
    frequency_map = defaultdict(list)
    num_rows = len(map_grid)
    num_cols = len(map_grid[0]) if map_grid else 0

    for x, row in enumerate(map_grid):
        for y, char in enumerate(row):
            if char != '.':
                frequency_map[char].append((x, y))
    antinode_positions = set()

    for character, positions in frequency_map.items():
        n = len(positions)
        if n < 2:
            continue  
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                dx = x2 - x1
                dy = y2 - y1

                C1_x = x1 - dx
                C1_y = y1 - dy
                C2_x = x2 + dx
                C2_y = y2 + dy

                if 0 <= C1_x < num_rows and 0 <= C1_y < num_cols:
                    antinode_positions.add((C1_x, C1_y))
                
                if 0 <= C2_x < num_rows and 0 <= C2_y < num_cols:
                    antinode_positions.add((C2_x, C2_y))
    return len(antinode_positions)

def part2(map_grid):
    frequency_map = defaultdict(list)
    num_rows = len(map_grid)
    num_cols = len(map_grid[0]) if map_grid else 0

    for x, row in enumerate(map_grid):
        for y, char in enumerate(row):
            if char != '.':
                frequency_map[char].append((x, y))
    antinode_positions = set()

    for character, positions in frequency_map.items():
        n = len(positions)
        if n < 2:
            continue  
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                dx, dy = x2 - x1, y2 - y1
                C1_x, C1_y = x1, y1
                C2_x, C2_y = x2, y2

                while  0 <= C1_x < num_rows and 0 <= C1_y < num_cols:
                    antinode_positions.add((C1_x, C1_y))
                    C1_x = C1_x - dx
                    C1_y = C1_y - dy

                while 0 <= C2_x < num_rows and 0 <= C2_y < num_cols:
                    antinode_positions.add((C2_x, C2_y))
                    C2_x = C2_x + dx
                    C2_y = C2_y + dy

    return len(antinode_positions)
    

if __name__=="__main__":
    print("\n--- Day 8: Resonant Collinearity ---")
    file = open("advent_of_code_2024/day8_input.txt","r")
    data1 = file.readlines()
    data = [x.strip() for x in data1]

    print("Part 1:")
    print(part1(data))
    print("Part 2:")
    print(part2(data))
    print()