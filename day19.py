
def make_onsen(onsen, blocks):
    n = len(onsen)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for block in blocks:
            k = len(block)
            if i - k >= 0 and onsen[i - k:i] == block:
                dp[i] += dp[i - k]
    # print(dp)
    return dp[n]


def part1(blocks, onsens):
    possible_designs = 0
    for onsen in onsens:
        # print(onsen)
        possible_designs += make_onsen(onsen, blocks) > 0
    return possible_designs

def part2(blocks, onsens):
    possible_designs = 0
    for onsen in onsens:
        # print(onsen)
        possible_designs += make_onsen(onsen, blocks)
    return possible_designs


if __name__=="__main__":
    print("\n--- Day 19: Linen Layout ---")
    file = open("advent_of_code_2024/day19_input.txt","r")
    data = [x.strip() for x in file.readlines()]
    # print(data)
    blocks_1 = data[0].split(',')
    blocks = [x.strip() for x in blocks_1]
    onsens = data[2:]
    # print(blocks)
    # print(onsens)

    print("Part 1:")
    print(part1(blocks, onsens))
    print("Part 2:")
    print(part2(blocks, onsens))
    print()
    