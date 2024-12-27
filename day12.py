def get_neighbours(x, y, rows, cols):
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            yield nx, ny


def find_connected_neighbours(x, y, grid, nset, visited):
    for nx, ny in get_neighbours(x, y, len(grid), len(grid[0])):
        if grid[nx][ny] == grid[x][y] and (nx, ny) not in nset:
            nset.add((nx, ny))
            visited.add((nx, ny))
            find_connected_neighbours(nx, ny, grid, nset, visited) 


def get_score_1(set_of_nodes, rows, cols):
    area = len(set_of_nodes)
    perimeter = 4 * area
    for x,y in set_of_nodes:
        for  nx, ny in get_neighbours(x, y, rows, cols):
            if (nx, ny) in set_of_nodes:
                perimeter -= 1
    return perimeter * area


def get_corners(set_of_nodes):
    corners = 0
    directions = [(0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1)]
    #               N       NE      E     SE      S      SW      W        NW
    for x,y in set_of_nodes:
        for i in range(4):
            # 1 and 2 are directions at right angles (NESW) and 3 is the direction between them
            dx1, dy1 = directions[i*2]
            x1, y1 = x+dx1, y+dy1
            dx2, dy2 = directions[(i*2+2)%8]
            x2, y2 = x+dx2, y+dy2
            dx3, dy3 = directions[(i*2+1)%8]
            x3, y3 = x+dx3, y+dy3

            # CONVEX CORNERS 
            # for cases like the following: (0 is in our region, x is not)
            # xx
            # x0
            if (x1,y1) not in set_of_nodes and (x2,y2) not in set_of_nodes:
                corners += 1

            # CONCAVE CORNERS
            # for cases like the following: (0 is in our region, x is not)
            # x0
            # 00
            elif (x1,y1) in set_of_nodes and (x2,y2) in set_of_nodes and (x3,y3) not in set_of_nodes:
                corners += 1
    return corners


def part1(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_cost = 0

    for x in range(rows):
        for y in range(cols):
            if (x,y) not in visited:
                nset = set()
                nset.add((x,y))
                visited.add((x,y))
                find_connected_neighbours(x, y, grid, nset, visited)
                total_cost += get_score_1(nset, rows, cols)
    return total_cost

    
def part2(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_cost = 0

    for x in range(rows):
        for y in range(cols):
            if (x,y) not in visited:
                nset = set()
                nset.add((x,y))
                visited.add((x,y))
                find_connected_neighbours(x, y, grid, nset, visited)
                area = len(nset)
                no_of_sides = get_corners(nset)
                total_cost += area * no_of_sides
    return total_cost

    
if __name__=="__main__":
    print("\n--- Day 12: Garden Groups ---")
    file = open("advent_of_code_2024/day12_input.txt","r")
    data1 = file.readlines()
    data = [x.strip() for x in data1]
    print("Part 1:")
    print(part1(data))
    print("Part 2:")
    print(part2(data))
    print()