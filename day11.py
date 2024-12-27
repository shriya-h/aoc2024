def part1(data):
    for _ in range(25):
        new_data = []
        for elem in data:
            if elem == '0':
                new_data.append('1')
            elif len(elem)%2 == 0:
                s1 = elem[ : len(elem)//2]
                s2 = elem[len(elem)//2 : ]
                new_data.append(str(int(s1)))
                new_data.append(str(int(s2)))
            else:
                new_data.append(str(int(elem)*2024))
        data = new_data
    return len(data)


def part2(data):
    dict = {}
    for item in data:
        dict[item] = dict.get(item,0) + 1
    for _ in range(75):
        new_dict = {}
        for key, value in dict.items():
            if key == '0':
                new_dict['1'] = new_dict.get('1', 0) + value
            elif len(key) % 2 == 0:
                right_half = str(int(key[ : len(key)//2]))
                left_half = str(int(key[len(key)//2 : ]))
                new_dict[right_half] = new_dict.get(right_half, 0) + value
                new_dict[left_half] = new_dict.get(left_half, 0) + value
            else:
                new_dict[str(int(key)*2024)] = new_dict.get(str(int(key)*2024), 0) + value
            dict = new_dict
    return sum(dict.values())
    

if __name__=="__main__":
    print("\n--- Day 11: Plutonian Pebbles ---")
    file = open("advent_of_code_2024/day11_input.txt","r")
    data = file.read().split()
    print("Part 1:")
    print(part1(data))
    print("Part 2:")
    print(part2(data))
    print()