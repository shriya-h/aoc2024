
def is_safe_report(levels):
    for i in range(len(levels)-1):
        if levels[i+1] - levels[i] > 3 or levels[i+1] - levels[i] < 1:
            return False
    return True

def part1(data):
    num_safe=0
    for report in data:
        words = report.split()
        levels = [int(x) for x in words]
        if is_safe_report(levels) or is_safe_report(levels[::-1]):
            num_safe += 1
    return num_safe

def part2(data):
    num_safe=0
    for report in data:
        words = report.split()
        levels = [int(x) for x in words]
        if is_safe_report(levels) or any([is_safe_report(levels[:i]+levels[i+1:]) for i in range(len(levels))]):
            num_safe += 1
        else:
            levels_reversed = levels[::-1]
            if is_safe_report(levels_reversed) or any([is_safe_report(levels_reversed[:i]+levels_reversed[i+1:]) for i in range(len(levels_reversed))]):
                num_safe += 1   
    return num_safe
    

if __name__=="__main__":
    print("\n--- Day 2: Red-Nosed Reports ---")
    file = open("advent_of_code_2024/day2_input.txt","r")
    data = file.readlines()
    
    print("Part 1:")
    print(part1(data))
    print("Part 2:")
    print(part2(data))
    print()