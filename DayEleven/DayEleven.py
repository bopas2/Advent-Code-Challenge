max_score = 0
best_coord = None

grid = []
for i in range(1, 301):
    grid.append([])
    for j in range(1, 301):
        temp_score = ((j + 10) * i + 2866) * (j + 10)
        if temp_score >= 100:
            temp_score = int(str((int(temp_score/100)))[-1:]) - 5
        else:
            temp_score = 0
        grid[i - 1].append(temp_score)

best_score = 0
best_coord = None
for i in range(1, 299):
    for j in range(1, 299):
        sum_score = 0
        x_offset = [-1, 0, 1]
        y_offset = [-1, 0, 1]
        for x in x_offset:
            for y in y_offset:
                sum_score += grid[i + y][j + x]
        if sum_score > best_score:
            best_score = sum_score
            best_coord = [j, i]
print('PART ONE: ')
print(best_coord)

max_score = 0
best_coord = []
cache = [x[:] for x in grid]
for size in range(1, 300):
    best_score = 0
    ok_coord = []
    for i in range(0, 300 - size + 1):
        for j in range(0, 300 - size + 1):
            temp_sum = cache[i][j]
            for tooAdd in range(size):
                temp_sum += grid[i + tooAdd][j + size - 1]
                temp_sum += grid[i + size - 1][j + tooAdd]
            temp_sum -= grid[i + size - 1][j + size - 1]  
            cache[i][j] = temp_sum  
            if temp_sum > best_score:
                best_score = temp_sum
                ok_coord = [j + 1, i + 1]
    if best_score > max_score:
        max_score = best_score
        best_coord = ok_coord + [size]
    print(size)
print(best_coord)