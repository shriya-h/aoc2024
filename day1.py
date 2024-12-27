def part1(list1_sorted, list2_sorted):
    ans=0
    for i in range(len(list1_sorted)):
        ans += abs(list1_sorted[i] - list2_sorted[i])
    return ans

def part2(list1_sorted, list2_sorted):
    list2_freq = {}
    ans = 0
    for num in list2_sorted:
        list2_freq[num] = list2_freq.get(num,0) + 1
    for num in list1_sorted:
        ans += num*list2_freq.get(num,0)
    return ans

if __name__=="__main__":
    print("\n--- Day 1: Historian Hysteria ---")
    file = open("advent_of_code_2024/day1_input.txt","r")
    data = file.readlines()
    list1=[]
    list2=[]

    for line in data:
        nums = line.split()
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))
    
    list1_sorted = sorted(list1)
    list2_sorted = sorted(list2)
    
    print("Part 1:")
    print(part1(list1_sorted, list2_sorted))
    print("Part 2:")
    print(part2(list1_sorted, list2_sorted))
    print()