def trailhead_score_1(grid, row, col, loc9):
    if grid[row][col] == 9:
        loc9.add((row,col))
        return
    
    directions = [[-1,0], [1,0], [0,-1], [0,1]]
    for direction in directions:
        curr_row = row + direction[0]
        curr_col = col + direction[1]
        if curr_row < 0 or curr_row >= len(grid) or curr_col < 0 or curr_col >= len(grid[0]) or (curr_row == row and curr_col == col):
            continue
        if grid[curr_row][curr_col] == grid[row][col] + 1:
            trailhead_score_1(grid, curr_row, curr_col,loc9)


def part1(grid):
    score = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                loc9 = set()
                trailhead_score_1(grid, row, col, loc9)
                curr_score = len(loc9)
                score += curr_score
                # print(f"row: {row}, col: {col}, score:{curr_score}")
    return score


def trailhead_score_2(grid, row, col):
    if grid[row][col] == 9:
        return 1
    
    num_curr_paths = 0
    directions = [[-1,0], [1,0], [0,-1], [0,1]]
    for direction in directions:
        curr_row = row + direction[0]
        curr_col = col + direction[1]
        if curr_row < 0 or curr_row >= len(grid) or curr_col < 0 or curr_col >= len(grid[0]) or (curr_row == row and curr_col == col):
            continue
        if grid[curr_row][curr_col] == grid[row][col] + 1:
            num_curr_paths += trailhead_score_2(grid, curr_row, curr_col)
    return num_curr_paths


def part2(grid):
    score = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                curr_score = trailhead_score_2(grid, row, col)
                score += curr_score
                # print(f"row: {row}, col: {col}, score:{curr_score}")
    return score


def parse_grid(data):
    grid=[]
    for line in data:
        row=[]
        for element in line:
            row.append(int(element))
        grid.append(row)
    return grid


if __name__=="__main__":
    print("\n--- Day 10: Hoof It ---")
    file = open("advent_of_code_2024/day10_input.txt","r")
    data1 = file.readlines()
    data = [x.strip() for x in data1]
    grid = parse_grid(data)
    # print(grid)
    print("Part 1:")
    print(part1(grid))
    print("Part 2:")
    print(part2(grid))
    print()