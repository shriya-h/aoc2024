import re2

def part1(data):
    patterns = ["XMAS", "X...\n.M..\n..A.\n...S"]
    return sum(len(re2.findall(pattern, data, rotate=True)) for pattern in patterns)


def part2(data):
    return len(re2.findall("M.M\n.A.\nS.S", data, rotate=True))
    

if __name__=="__main__":
    print("\n--- Day 4: Ceres Search ---")
    file = open("advent_of_code_2024/day4_input.txt","r")
    data = file.read()
    
    print("Part 1:")
    print(part1(data))
    print("Part 2:")
    print(part2(data))
    print()