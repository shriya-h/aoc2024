def can_make_target(answer, operands):
    from itertools import product

    def evaluate_expression(ops):
        result = operands[0]
        for i, op in enumerate(ops):
            if op == '+':
                result += operands[i + 1]
            elif op == '*':
                result *= operands[i + 1]
        return result

    num_operators = len(operands) - 1
    for operator_set in product(['+', '*'], repeat=num_operators):
        if evaluate_expression(operator_set) == answer:
            return True
    return False

def can_make_target_with_concatenation(answer, operands):
    from itertools import product

    def evaluate_expression(ops):
        result = operands[0]
        for i, op in enumerate(ops):
            if op == '+':
                result += operands[i + 1]
            elif op == '*':
                result *= operands[i + 1]
            elif op == '||':
                result = int(str(result) + str(operands[i + 1]))
        return result

    # Generate all possible operator combinations ('+', '*', '||') for len(operands) - 1 slots
    num_operators = len(operands) - 1
    for operator_set in product(['+', '*', '||'], repeat=num_operators):
        if evaluate_expression(operator_set) == answer:
            return True
    return False


def part1(data):
    result = 0
    for line in data:
        answer_and_operands = line.split(':')
        answer = int(answer_and_operands[0])
        operands_1 = answer_and_operands[1].split(' ')
        operands = [int(x.strip()) for x in operands_1 if x.strip().isdigit()]
        if can_make_target(answer, operands):
            result += answer
    return result


def part2(data):
    result = 0
    for line in data:
        answer_and_operands = line.split(':')
        answer = int(answer_and_operands[0])
        operands_1 = answer_and_operands[1].split(' ')
        operands = [int(x.strip()) for x in operands_1 if x.strip().isdigit()]
        if can_make_target_with_concatenation(answer, operands):
            result += answer
    return result
    

if __name__=="__main__":
    print("\n--- Day 7: Bridge Repair ---")
    file = open("advent_of_code_2024/day7_input.txt","r")
    data = file.readlines()
    
    print("Part 1:")
    print(part1(data))
    print("Part 2:")
    print(part2(data))
    print()