from sys import maxsize
from itertools import pairwise, permutations

dir_base_lookup = {
    ('A', 'A'): 'A',
    ('^', '^'): 'A',
    ('>', '>'): 'A',
    ('v', 'v'): 'A',
    ('<', '<'): 'A',
    ('A', '^'): '<A',
    ('^', 'A'): '>A',
    ('A', '>'): 'vA',
    ('>', 'A'): '^A',
    ('v', '^'): '^A',
    ('^', 'v'): 'vA',
    ('v', '<'): '<A',
    ('<', 'v'): '>A',
    ('v', '>'): '>A',
    ('>', 'v'): '<A',

    ('A', 'v'): 'v<A',
    ('v', 'A'): '>^A',
    ('A', '<'): 'v<<A',
    ('<', 'A'): '>>^A',

    ('>', '<'): '<<A',
    ('<', '>'): '>>A',
    ('<', '^'): '>^A',
    ('^', '<'): 'v<A',
    ('>', '^'): '<^A',
    ('^', '>'): 'v>A',
}

dirs = [
    [('^', -1), ('v', 1)],
    [('<', -1), ('>', 1)],
]

numpad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A']
]

numpad_lookup = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    ' ': (3, 0), '0': (3, 1), 'A': (3, 2),
}

dirpad = [
    [' ', '^', 'A'],
    ['<', 'v', '>'],
]

dirpad_lookup = {
    ' ': (0, 0), '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}

memo_dir = {} # TODO memo
def dir_dfs(key_start, key_end, depth=0):
    if depth == 0:
        return dir_base_lookup[key_start, key_end]

    s = dir_dfs(key_start, key_end, depth-1)
    out = ""
    for k0, k1 in pairwise('A' + s):
        out += dir_base_lookup[k0, k1]

    return out

memo_num = {} # TODO memo
def num_solve(key_start, key_end):
    print("num_solve", key_start, key_end)
    y0, x0 = numpad_lookup[key_start]
    y1, x1 = numpad_lookup[key_end]
    y_dist, x_dist = y1 - y0, x1 - x0
    y_key, y_dir = dirs[0][y_dist > 0]
    x_key, x_dir = dirs[1][x_dist > 0]

    # To dodge blank corner
    start_move = ""
    mov_s = ""
    if (y0 == 3 or y1 == 3) and (x0 == 0 or x1 == 0):
        if x0 == 0:
            start_move = '>'
            mov_s = y_key * abs(y_dist) + x_key * (abs(x_dist) - 1)
        else:
            start_move = '^'
            mov_s = y_key * (abs(y_dist) - 1) + x_key * abs(x_dist)
    else:
        mov_s = y_key * abs(y_dist) + x_key * abs(x_dist)

    possible_inputs = [
        'A' + start_move + ''.join(x) + 'A'
        for x in set(permutations(mov_s))
    ]
    print("possible inputs", possible_inputs)

    min_score, min_inputs = maxsize, ""
    for inputs in possible_inputs:
        print(inputs)
        sequence = ''.join(dir_dfs(k0, k1, depth=1) for k0, k1 in pairwise(inputs))
        print(sequence)
        if len(sequence) < min_score:
            min_score = len(sequence)
            min_inputs = sequence
    memo_num[key_start, key_end] = min_score
    print("best input", min_inputs, "score", min_score)

    return min_inputs

def reduce_print_nums(s):
    k2d = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

    out = ""

    y, x = (3, 2)
    for c in s:
        if c == 'A':
            out += numpad[y][x]
            continue
        dy, dx = k2d[c]
        y, x = y+dy, x+dx
        if numpad[y][x] == ' ':
            print("blank panic", y, x, s, out)
            assert(False)
    print(out)

def reduce_print(s, depth):
    if depth <= 0:
        reduce_print_nums(s)
        return

    k2d = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

    out = ""
    y, x = (0, 2)
    for c in s:
        if c == 'A':
            out += dirpad[y][x]
            continue
        dy, dx = k2d[c]
        y, x = y+dy, x+dx
        if dirpad[y][x] == ' ':
            print("blank panic", y, x, s, out)
            assert(False)

    print(out)
    reduce_print(out, depth - 1)

if __name__ == "__main__":
    codes = open("advent_of_code_2024/day21_input.txt").read().splitlines()
    out = 0
    for code in codes:
        m = int(code[:-1])
        s = ''.join(num_solve(a, b) for a, b in pairwise("A" + code))
        out += len(s) * m
        print("code", code, "gives", s, "len", len(s), "score", len(s) * m)
        reduce_print(s, 2)
    print("overall score", out)