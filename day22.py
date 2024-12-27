import time
import math

def next_secret_number(n):
     return (((((n ^ (n << 6)) & 0xFFFFFF) ^ (((n ^ (n << 6)) & 0xFFFFFF) >> 5)) & 0xFFFFFF) ^ (((((n ^ (n << 6)) & 0xFFFFFF) ^ (((n ^ (n << 6)) & 0xFFFFFF) >> 5)) & 0xFFFFFF) << 11)) & 0xFFFFFF

def part1(nums):
    sum = 0
    for num in nums:
        for _ in range(2000):
            num = next_secret_number(num)
        sum += num
        # print(num)
    return sum

def part2(nums):
    sum = 0
    REPETITIONS = 2000
    sequences = []
    changes = []    
    for num in nums:
        sequence = [num % 10]
        change = []
        for i in range(0, REPETITIONS):
            prev = num
            num = next_secret_number(num)

            sequence.append(num % 10)
            change.append(num % 10 - prev % 10)

        #print(f"After {REPETITIONS} repetitions, number {number.strip()} became {num}")
        sum += num
        sequences.append(sequence)
        changes.append(change)

    # print(f"Lists of sequences and changes created.")
    # print(f"{sequences=}")
    # print(f"{changes=}")

    quadruples = []
    for number in range(0, len(sequences)):
        quadruple = {}
        for i in range(3, REPETITIONS):
            name = "{:+}".format(changes[number][i-3]) + "{:+}".format(changes[number][i-2]) + "{:+}".format(changes[number][i-1]) + "{:+}".format(changes[number][i])
            if name not in quadruple:
                quadruple[name] = sequences[number][i+1]
        quadruples.append(quadruple)
    
    # print(f"{quadruples=}")

    sums = {}
    for number in range(0, len(sequences)):
        for key, value in quadruples[number].items():
            sums[key] = sums.get(key, 0) + value

    # print(f"{sums=}")            

    # print(f"Maximal number of bananas one can get is {max(sums.values())}.") 
    return max(sums.values())   

if __name__=="__main__":
    print("\n--- Day 22: Monkey Market ---")
    file = open("advent_of_code_2024/day22_input.txt","r")
    data = [int(x.strip()) for x in file.readlines()]
    # print(data)

    print("Part 1:")
    start1 = time.time()
    print(part1(data))
    end1 = time.time()
    print(f"Elapsed time: {end1-start1:.4f} seconds")

    print("Part 2:")
    start2 = time.time()
    print(part2(data))
    end2 = time.time()
    print(f"Elapsed time: {end2-start2:.4f} seconds")
    print()