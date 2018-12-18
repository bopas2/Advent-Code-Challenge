import sys
import copy

with open('input.txt') as file:
        inp = file.read().strip().split('\n')
tea = []
for i in inp:
    tea.append(list(i))
inp = tea

def count_surrounding(X, Y, key):
    global inp
    xs = [-1, 0, 1]
    ys = [-1, 0, 1]
    count = 0
    for i in xs:
        for j in ys:
            if X + i >= 0 and X + i < len(inp[0]):
                if Y + j >= 0 and Y + j < len(inp):
                    if j != 0 or i != 0:
                        if inp[Y + j][X + i] == key:
                            count += 1
    return count

def print_grid(grid):
    for i in grid:
        for j in i:
            sys.stdout.write(str(j))
        print()
    print()

def calc_wood_count():
    lumber_count = 0
    wooded_count = 0
    for i in inp:
        for j in i:
            if j == "#":
                lumber_count += 1
            if j == "|":
                wooded_count += 1
    return (wooded_count * lumber_count)

def recall(history, current):
    for z, h in enumerate(history):
        seen = True
        for y, i in enumerate(h):
            if not seen:
                break
            for x, j in enumerate(i):
                if current[y][x] != j:
                    seen = False
                    break
        if seen:
            return z
    return -1

def create_wood_map(num_iters):
    global inp
    global tea
    history = []

    for z in range(num_iters):
        temp = [x[:] for x in inp]
        for y, i in enumerate(inp):
            for x, j in enumerate(i):
                if j == '.':
                    if count_surrounding(x, y, '|') >= 3:
                        temp[y][x] = '|'
                if j == '#':
                    if count_surrounding(x, y, '#') < 1 or count_surrounding(x, y, '|') < 1:
                        temp[y][x] = '.'
                if j == '|':
                    if count_surrounding(x, y, '#') >= 3:
                        temp[y][x] = '#'
        inp = temp
        when = recall(history, inp)
        if when != -1:
            inp = history[(1000000000 - z) % (len(history) - when) + when - 1]
            break
        history.append([x[:] for x in inp])
    print(calc_wood_count())
    inp = tea

print("PART ONE: ")
create_wood_map(10)
print("PART TWO: ")
create_wood_map(1000000000)

