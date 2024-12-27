import re

def part1(data):
    ans=0
    pattern = r"mul\((\d+),(\d+)\)"
    for line in data:
        matches = re.findall(pattern, line)
        ans += sum(int(x)*int(y) for x,y in matches)
    return ans

def part2(data):
    matching_pattern = r"mul\((\d+),(\d+)\)"
    control_pattern = r"do\(\)|don't\(\)"
    combined_pattern = fr"({matching_pattern})|({control_pattern})"
    mul_enabled = True
    total = 0
    for corrupted_memory in data:
        matches = re.finditer(combined_pattern, corrupted_memory)
        for match in matches:
            if match.group(1):  # If it's a valid mul(X,Y) instruction
                if mul_enabled:
                    x, y = int(match.group(2)), int(match.group(3))  # Use correct groups
                    total += x * y
            elif match.group(4):  # If it's a control instruction
                if match.group(4) == "do()":  # Enable mul instructions
                    mul_enabled = True
                elif match.group(4) == "don't()":  # Disable mul instructions
                    mul_enabled = False
    return total
    

if __name__=="__main__":
    print("\n--- Day 3: Mull It Over ---")
    file = open("advent_of_code_2024/day3_input.txt","r")
    data = file.readlines()
    
    print("Part 1:")
    print(part1(data))
    print("Part 2:")
    print(part2(data))
    print()