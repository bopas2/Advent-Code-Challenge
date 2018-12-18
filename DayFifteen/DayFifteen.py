class Unit:
    def __init__(self, type):
        self.type = type # A boolean, True means Elf, false means goblin
        self.HP = 200

with open('input.txt') as file:
        inp = file.read().strip().split('\n')

grid = []
for i in inp:
    toAdd = []
    for j in i:
        if j == '#':
            toAdd.append('#')
        if j == '.':
            toAdd.append(".")
        if j == "E":
            toAdd.append(Unit(True))
        else:
            toAdd.append(Unit(False))
    grid.append(toAdd)

def game_completed():
    return False

def move(person, X, Y):
    path = bfs_recursive(person, X, Y, [])
    if path == []:
        return
    if path[0] == 'U':
        grid[Y - 1][X] = grid[Y][X]
        grid[Y][X] = '.'
    if path[0] == 'L':
        grid[Y][X - 1] = grid[Y][X]
        grid[Y][X] = '.'
    if path[0] == 'R':
        grid[Y][X + 1] = grid[Y][X]
        grid[Y][X] = '.'
    if path[0] == 'D':
        grid[Y + 1][X] = grid[Y][X]
        grid[Y][X] = '.'

def near_enemy(person, X, Y):
    if X + 1 < len(grid[0]): 
        if isinstance(grid[Y][X + 1], Unit) and grid[Y][X + 1].type != person.type:
            grid[Y][X + 1].hp -= 3
            return True
    if X - 1 >= 0:
        if isinstance(grid[Y][X - 1], Unit) and grid[Y][X - 1].type != person.type:
            grid[Y][X - 1].hp -= 3
            return True
    if Y + 1 < len(grid):
        if isinstance(grid[Y + 1][X], Unit) and grid[Y + 1][X].type != person.type:
            grid[Y + 1][X].hp -= 3
            return True
    if Y - 1 >= 0:
        if isinstance(grid[Y - 1][X], Unit) and grid[Y  -1][X].type != person.type:
            grid[Y - 1][X].hp -= 3
            return True
    return False

def bfs_recursive(person, X, Y, path):
    if near_enemy(person.type, X, Y): 
        return path
    if Y - 1 >= 0 and grid[Y-1][X] == ".":
        return bfs_recursive(person, X, Y - 1, path.append('U'))
    if X - 1 >= 0 and grid[Y][X-1] == ".":
        return bfs_recursive(person, X - 1, Y, path.append('L'))
    if X + 1 < len(Y[0]) and grid[Y][X+1] == ".":
        return bfs_recursive(person, X + 1, Y, path.append('R'))
    if Y + 1 < len(Y) and grid[Y+1][X] == ".":
        return bfs_recursive(person, X, Y + 1, path.append('D'))
    return path

count = 0
while not game_completed():
    for y, i in enumerate(grid):
        for x, j in enumerate(i):
            if j != '#' and j != '.':
                move(j, x, y)
    count += 1




