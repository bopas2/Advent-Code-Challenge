import sys

def detect_message(data):
    nodes_connected = 0
    total_nodes = len(data)
    for i in data:
        for j in data:
            if detect_connection(i[0][0], i[0][1], j[0][0], j[0][1]):
                nodes_connected += 1
                break
    if nodes_connected / total_nodes >= 1:
        return True
    return False

def detect_connection(x1, y1, x2, y2):
    if y1 == y2 and (x1 + 1 == x2 or x1 - 1 == x2):
        return True
    if x1 == x2 and (y1 + 1 == y2 or y1 - 1 == y2):
        return True
    if y1 + 1 == y2 and x1 + 1 == x2:
        return True
    if x1 - 1 == x2 and y1 + 1 == y2:
        return True
    if y1 - 1 == y2 and x1 + 1 == x2:
        return True
    if x1 - 1 == x2 and y1 - 1 == y2:
       return True
    return False

def print_grid(data):
    smallest_x = data[0][0][0]
    smallest_y = data[0][0][1]
    largest_x = data[0][0][0]
    largest_y = data[0][0][1]
    for i in data:
        if i[0][0] < smallest_x:
            smallest_x = i[0][0]
        if i[0][1] < smallest_y:
            smallest_y = i[0][1]
        if i[0][0] > largest_x:
            largest_x = i[0][0]
        if i[0][1] > largest_y:
            largest_y = i[0][1]
    grid = []
    wid = int(largest_x - smallest_x) + 1
    ht = int(largest_y - smallest_y) + 1
    for y in range(ht):
        grid.append([])
        for x in range(wid):
            grid[y].append(0)
    for j in data:
        grid[int(j[0][1] - smallest_y)][int(j[0][0] - smallest_x)] += 1
    for y in range(ht):
        for x in range(wid):
            if grid[y][x] == 0:
                grid[y][x] = ' '
    for y in range(ht):
        for x in range(wid):
            sys.stdout.write(str(grid[y][x]))
        print()
    print()
    print()

with open('input.txt') as file:
        inp = file.read().strip().split('\n')

# inp = list(map(lambda x: [[float(x[10:12].strip()), float(x[14:16].strip())],[float(x[28:30].strip()),float(x[32:34].strip())]], inp))
inp = list(map(lambda x: [[float(x[10:16].strip()), float(x[18:24].strip())],[float(x[36:38].strip()),float(x[40:42].strip())]], inp))

# find when two points almost intercept (solve linear equation with velocity as slope with error instead of percise interception)
# abs(inp[0][0][0] + inp[0][1][0] * x - (inp[1][0][0] + inp[1][1][0] * x)) <= 30
estimated_time_of_convergence = abs(int(((inp[0][0][0] - inp[1][0][0])) / (inp[0][1][0] - inp[1][1][0])))
time_to_converge = estimated_time_of_convergence
for j in inp:
    j[0][0] += estimated_time_of_convergence * j[1][0]
    j[0][1] += estimated_time_of_convergence * j[1][1]

while True:
    if detect_message(inp):
        print("Part 1: ")
        print_grid(inp)
        print("Part 2: ")
        print(time_to_converge)
        break
    else:
        for j in inp:
            j[0][0] += j[1][0]
            j[0][1] += j[1][1]
        time_to_converge += 1