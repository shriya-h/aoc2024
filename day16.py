import heapq 

def solve(map, start, end):
    DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
    R = len(map)
    C = len(map[0])
    G = map
    sr, sc = start
    er, ec = end
    Q = []
    SEEN = set()
    heapq.heappush(Q, (0,sr,sc,1))
    DIST = {}
    best = None
    while Q:
        d,r,c,dir = heapq.heappop(Q)
        if (r,c,dir) not in DIST:
            DIST[(r,c,dir)] = d
        if r==er and c==ec and best is None:
            best = d
        if (r,c,dir) in SEEN:
            continue
        SEEN.add((r,c,dir))
        dr,dc = DIRS[dir]
        rr,cc = r+dr,c+dc
        if 0<=cc<C and 0<=rr<R and G[rr][cc] != '#':
            heapq.heappush(Q, (d+1, rr,cc,dir))
        heapq.heappush(Q, (d+1000, r,c,(dir+1)%4))
        heapq.heappush(Q, (d+1000, r,c,(dir+3)%4))
    print("Part 1:")
    print(best)


    Q = []
    SEEN = set()
    for dir in range(4):
        heapq.heappush(Q, (0,er,ec,dir))
    DIST2 = {}
    while Q:
        d,r,c,dir = heapq.heappop(Q)
        if (r,c,dir) not in DIST2:
            DIST2[(r,c,dir)] = d
        if (r,c,dir) in SEEN:
            continue
        SEEN.add((r,c,dir))
        # going backwards instead of forwards here
        dr,dc = DIRS[(dir+2)%4]
        rr,cc = r+dr,c+dc
        if 0<=cc<C and 0<=rr<R and G[rr][cc] != '#':
            heapq.heappush(Q, (d+1, rr,cc,dir))
        heapq.heappush(Q, (d+1000, r,c,(dir+1)%4))
        heapq.heappush(Q, (d+1000, r,c,(dir+3)%4))

    OK = set()
    for r in range(R):
        for c in range(C):
            for dir in range(4):
                # (r,c,dir) is on an optimal path if the distance from start to end equals the distance from start to (r,c,dir) plus the distance from (r,c,dir) to end.
                if (r,c,dir) in DIST and (r,c,dir) in DIST2 and DIST[(r,c,dir)] + DIST2[(r,c,dir)] == best:
                    OK.add((r,c))
    print("Part 2:")
    print(len(OK))

if __name__=="__main__":
    print("\n--- Day 16: Reindeer Maze ---")
    file = open("advent_of_code_2024/day16_input.txt","r")
    data = [x.strip() for x in file.readlines()]
    # print(data)
    for i,line in enumerate(data):
        for j,c in enumerate(line):
            if c=="S":
                # print(f"Start S: {i},{j}")
                start = (i,j)
            if c=="E":
                # print(f"End E: {i},{j}")
                end = (i,j)
    solve(data, start, end)
    # print("Part 2:")
    # print(part2(data))