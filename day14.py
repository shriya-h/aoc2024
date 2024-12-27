import re
import numpy as np
import matplotlib.pyplot as plt

def parse_input(data):
    robots = []
    for line in data:
        p_match = re.search(r"p=(-?\d+),(-?\d+)", line)
        v_match = re.search(r"v=(-?\d+),(-?\d+)", line)
        if p_match and v_match:
            px, py = map(int, p_match.groups())
            vx, vy = map(int, v_match.groups())
            robots.append({'p': (px, py), 'v': (vx, vy)})
    return robots


def part1(robots):
    time = 100
    width = 101
    height = 103

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for robot in robots:
        px, py = robot['p']
        vx, vy = robot['v']
        
        # Compute new position after `time` seconds with wrapping
        x_new = (px + time * vx) % width
        y_new = (py + time * vy) % height

        if x_new < width//2:
            if y_new < height//2:
                q4 += 1
            elif y_new > height//2:
                q3 += 1
        elif x_new > width//2:
            if y_new < height//2:
                q2 += 1
            elif y_new > height//2:
                q1 += 1
    print(q1*q2*q3*q4)

def entropy(img):
    marg = np.histogramdd(np.ravel(img), bins = 256)[0]/img.size
    marg = list(filter(lambda p: p > 0, np.ravel(marg)))
    entropy = -np.sum(np.multiply(marg, np.log2(marg)))
    return entropy

def move_robots(robots,xmax,ymax):
    newrobots = []
    # print(robots)
    for robot in robots:
        px, py = robot['p']
        vx, vy = robot['v']
        x = (px + vx) % xmax
        y = (py + vy) % ymax
        newrobots.append({'p': (x, y), 'v': (vx, vy)})
    return newrobots


def robots_to_grid(robots,xmax,ymax):
    grid = np.zeros((ymax,xmax),dtype=int)
    # print(robots)
    for robot in robots:
        x,y = robot['p']
        grid[y,x] += 1
    return grid

def part2(robots):
    xmax = 101
    ymax = 103
    entropies = []
    for i in range(10000):   
        # print(f"Iter: {i}")     
        newrobots = move_robots(robots,xmax,ymax)
        grid = robots_to_grid(newrobots,xmax,ymax)
        entropies.append(entropy(grid))
        robots = newrobots

    fig, ax = plt.subplots(figsize=(8,6),dpi=100)

    plt.plot([i+1 for i in range(10000)],entropies,linestyle="",marker=".")

    ax.set_xlabel("time (s)")
    ax.set_ylabel("entropy")

    easter_egg = entropies.index( min(entropies) )+1
    plt.plot(easter_egg,entropies[easter_egg-1],linestyle="",marker="o")
    plt.savefig('advent_of_code_2024/day14plot.png') 

    print(easter_egg)



if __name__=="__main__":
    print("\n--- Day 14: Restroom Redoubt ---")
    file = open("advent_of_code_2024/day14_input.txt","r")
    data = [x.strip() for x in file.readlines()]
    robots = parse_input(data)
    # print(robots)
    print("Part 1:")
    part1(robots.copy())
    print("Part 2:")
    part2(robots.copy())
    print()