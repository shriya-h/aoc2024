import re
from math import gcd


def parse_input_1(data):
    machines = []
    for i in range(0, len(data), 4):
        button_a = list(map(int, re.findall(r"-?\d+", data[i])))
        button_b = list(map(int, re.findall(r"-?\d+", data[i+1])))
        prize = list(map(int, re.findall(r"-?\d+", data[i+2])))
        machines.append({
            'A': {'x': button_a[0], 'y': button_a[1]},
            'B': {'x': button_b[0], 'y': button_b[1]},
            'prize': {'x': prize[0], 'y': prize[1]}
        })
    return machines


def calculate_cost_1(machine):
    ax, ay = machine['A']['x'], machine['A']['y']
    bx, by = machine['B']['x'], machine['B']['y']
    px, py = machine['prize']['x'], machine['prize']['y']
    min_cost = 100000000000
    found_solution = False

    for a_presses in range(101):
        for b_presses in range(101):
            x_reached = a_presses * ax + b_presses * bx
            y_reached = a_presses * ay + b_presses * by

            if x_reached == px and y_reached == py:
                found_solution = True
                cost = a_presses * 3 + b_presses * 1
                min_cost = min(min_cost, cost)


    return min_cost if found_solution else 0


def part1(data):
    machines = parse_input_1(data)
    total_cost = 0

    for machine in machines:
        cost = calculate_cost_1(machine)
        total_cost += cost
    return total_cost


def parse_input_2(data):
    machines = []
    for i in range(0, len(data), 4):
        button_a = list(map(int, re.findall(r"-?\d+", data[i])))
        button_b = list(map(int, re.findall(r"-?\d+", data[i+1])))
        prize = list(map(int, re.findall(r"-?\d+", data[i+2])))
        machines.append({
            'A': {'x': button_a[0], 'y': button_a[1]},
            'B': {'x': button_b[0], 'y': button_b[1]},
            'prize': {'x': prize[0] + 10000000000000, 'y': prize[1] + 10000000000000}
        })
    return machines


def calculate_cost_2(machine):
    ax, ay = machine['A']['x'], machine['A']['y']
    bx, by = machine['B']['x'], machine['B']['y']
    px, py = machine['prize']['x'], machine['prize']['y']

    b, brem = divmod(ay * px - ax * py, ay * bx - ax * by)
    a, arem = divmod(px - b * bx, ax)
    return 0 if arem or brem else a * 3 + b


def part2(data):
    machines = parse_input_2(data)
    total_cost = 0

    for machine in machines:
        cost = calculate_cost_2(machine)
        total_cost += cost
    return total_cost
    

if __name__=="__main__":
    print("\n--- Day 13: Claw Contraption ---")
    file = open("advent_of_code_2024/day13_input.txt","r")
    data = [x.strip() for x in file.readlines()]
    data.append('')
    # print(data)
    print("Part 1:")
    print(part1(data))
    print("Part 2:")
    print(part2(data))
    print()