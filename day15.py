
def part1(grid, moves):
    grid = [list(row) for row in grid]

    # Define movement directions
    direction_map = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}

    # Find the robot's initial position
    robot_position = None
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '@':
                robot_position = (r, c)
                break

    # Simulate each move
    for move in moves:
        dr, dc = direction_map[move]
        robot_r, robot_c = robot_position
        new_robot_r, new_robot_c = robot_r + dr, robot_c + dc

        # Check if the new robot position is within bounds and not a wall
        if grid[new_robot_r][new_robot_c] == '.':
            # Move the robot to the new position
            grid[robot_r][robot_c] = '.'
            grid[new_robot_r][new_robot_c] = '@'
            robot_position = (new_robot_r, new_robot_c)

        elif grid[new_robot_r][new_robot_c] == 'O':
            # Try to push the box
            box_r, box_c = new_robot_r, new_robot_c
            push_r, push_c = box_r, box_c

            while grid[push_r][push_c] == 'O':
                push_r, push_c = push_r + dr, push_c + dc

            # Check if the box can be pushed (must be empty space)
            if grid[push_r][push_c] == '.':
                # Move the box
                grid[box_r][box_c] = '.'
                grid[push_r][push_c] = 'O'

                # Move the robot to the new position
                grid[robot_r][robot_c] = '.'
                grid[new_robot_r][new_robot_c] = '@'
                robot_position = (new_robot_r, new_robot_c)
    
    total_sum = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 'O':
                gps = 100 * r + c
                total_sum += gps
    return total_sum


if __name__=="__main__":
    print("\n--- Day 15: Warehouse Woes ---")
    file = open("advent_of_code_2024/day15_input.txt","r")
    data = [x.strip() for x in file.readlines()]
    grid = []
    for i in range(50):
        grid.append(data[i])
    movements_list = []
    for i in range(51,71,1):
        movements_list.append(data[i])
    moves = ''.join(movements_list)

    print("Part 1:")
    print(part1(grid, moves))


