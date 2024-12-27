import time

def parse_input(data):
    rows = 7
    cols = 5
    lock_grids = []
    key_grids = []

    all_data = data.split('\n\n')
    for item in all_data:
        piece = item.split('\n')
        if piece[0] == '.....' and piece[-1] == '#####':
            key_grids.append(piece)
        elif piece[0] == '#####' and piece[-1] == '.....':
            lock_grids.append(piece)
    
    locks = []
    keys = []

    for lock in lock_grids:
        curr_lock = []
        for j in range(cols):
            i = 0
            while i < rows and lock[i][j] == '#':
                i += 1
            curr_lock.append(i-1)
        locks.append(curr_lock)

    for key in key_grids:
        curr_key = []
        for j in range(cols):
            i = rows - 1
            while i >= 0 and key[i][j] == '#':
                i -= 1
            curr_key.append(5 - i)
        keys.append(curr_key)

    # print(lock_grids)
    # print(key_grids)
    # print(locks)
    # print(keys)

    return locks, keys


def part1(locks, keys):
    valid_pairs = 0
    for lock in locks:
        for key in keys:
            isValid = True
            for i in range(5):
                if lock[i] + key[i] > 5:
                    isValid = False
                    break
            if isValid:
                # print(lock, key)
                valid_pairs += 1
    
    return valid_pairs

if __name__=="__main__":
    print("\n--- Day 25: Code Chronicle ---")
    file = open("advent_of_code_2024/day25_input.txt","r")
    data = file.read()
    # parse_input(data)
    locks, keys = parse_input(data)
    # print(data)

    print("Part 1:")
    start1 = time.time()
    print(part1(locks, keys))
    end1 = time.time()
    print(f"Elapsed time: {end1-start1:.4f} seconds")

    # print("Part 2:")
    # start2 = time.time()
    # print(part2(graph))
    # end2 = time.time()
    # print(f"Elapsed time: {end2-start2:.4f} seconds")
    # print()