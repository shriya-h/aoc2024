def part1(grid):
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (row_change, col_change)
    dir_symbols = ['^', '>', 'v', '<']
    height = len(grid)
    width = len(grid[0])
    
    # Find the starting position and direction
    for r in range(height):
        for c in range(width):
            if grid[r][c] in dir_symbols:
                start_pos = (r, c)
                direction = dir_symbols.index(grid[r][c])
                break
    
    visited = set()
    current_pos = start_pos
    
    while True:
        # Mark the current position as visited
        visited.add(current_pos)
        r, c = current_pos
        dr, dc = directions[direction]
        
        # Calculate the next position
        next_pos = (r + dr, c + dc)
        next_r, next_c = next_pos
        
        # Check if the next position is valid
        if (0 <= next_r < height and 0 <= next_c < width and grid[next_r][next_c] != '#'):
            # Move forward
            current_pos = next_pos
        else:
            # Turn right
            direction = (direction + 1) % 4
        
        # Stop if the guard leaves the grid
        if not (0 <= next_r < height and 0 <= next_c < width):
            break
    
    return len(visited)

def simulate_guard_path_with_obstruction(grid, obstruction_pos):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (row_change, col_change)
    dir_symbols = ['^', '>', 'v', '<']
    height = len(grid)
    width = len(grid[0])
    
    # Find the starting position and direction
    for r in range(height):
        for c in range(width):
            if grid[r][c] in dir_symbols:
                start_pos = (r, c)
                direction = dir_symbols.index(grid[r][c])
                break

    visited = set()
    current_pos = start_pos
    path_states = set()

    while True:
        # Mark the current position and direction
        state = (current_pos, direction)
        if state in path_states:
            return True  # Cycle detected
        path_states.add(state)
        
        r, c = current_pos
        dr, dc = directions[direction]
        next_pos = (r + dr, c + dc)
        next_r, next_c = next_pos
        
        # Check if the next position is valid
        if next_pos == obstruction_pos or not (0 <= next_r < height and 0 <= next_c < width) or grid[next_r][next_c] == '#':
            # Turn right
            direction = (direction + 1) % 4
        else:
            # Move forward
            current_pos = next_pos
        
        # Stop if the guard leaves the grid
        if not (0 <= next_r < height and 0 <= next_c < width):
            return False

def part2(grid):
    height = len(grid)
    width = len(grid[0])
    valid_positions=0

    for r in range(height):
        for c in range(width):
            if (grid[r][c]=="."):
                obstruction_pos = (r,c)
                # print("Obstruction at position: ", obstruction_pos)
                if simulate_guard_path_with_obstruction(grid, obstruction_pos):
                    valid_positions += 1
    return valid_positions
    
    

if __name__=="__main__":
    print('\n--- Day 6: Guard Gallivant ---')
    file = open("advent_of_code_2024/day6_input.txt","r")
    data1 = file.readlines()
    data = [s.rstrip('\n') for s in data1]
    
    print("Part 1:")
    print(part1(data))
    print("Part 2:")
    print(part2(data))
    print()