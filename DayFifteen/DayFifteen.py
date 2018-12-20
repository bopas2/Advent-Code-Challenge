import queue
import sys

class Unit:
    def __init__(self, data, x, y):
        self.type = data # A boolean, True means Elf, False means goblin
        self.HP = 200
        self.xpos = x
        self.ypos = y
    def __str__(self):
        if self.type:
            return f'E'
        return f'G'

with open('input.txt') as file:
        inp = file.read().strip().split('\n')
ELVES = []
Elf_count = 0
Gob_count = 0
GOBLINS = []
grid = []
for y, i in enumerate(inp):
    toAdd = []
    for x, j in enumerate(i):
        if j == '#':
            toAdd.append('#')
        if j == '.':
            toAdd.append(".")
        if j == "E":
            newElf = Unit(True, x, y)
            toAdd.append(newElf)
            ELVES.append(newElf)
            Elf_count += 1
        if j == 'G':
            newGob = Unit(False, x, y)
            toAdd.append(newGob)
            GOBLINS.append(newGob)
            Gob_count += 1
    grid.append(toAdd)

orig_elf_count = Elf_count
orig_gob_count = Gob_count

def print_grid(grid):
    for i in grid:
        for j in i:
            sys.stdout.write(str(j))
        print()
    print()

def game_completed():
    return Elf_count == 0 or Gob_count == 0

def attack(person, game_map, attack_dmg):
    if game_map[person.ypos][person.xpos] != person:
        return
    global Elf_count
    global Gob_count
    lowestHP = 300
    xOffset = 0
    yOffset = 0
    if person.ypos - 1 >= 0 and isinstance(game_map[person.ypos - 1][person.xpos], Unit) and game_map[person.ypos - 1][person.xpos].type != person.type:
        if game_map[person.ypos - 1][person.xpos].HP < lowestHP:
            lowestHP = game_map[person.ypos - 1][person.xpos].HP
            xOffset = 0
            yOffset = -1
    
    if person.xpos - 1 >= 0 and isinstance(game_map[person.ypos][person.xpos - 1], Unit) and game_map[person.ypos][person.xpos - 1].type != person.type:
        if game_map[person.ypos][person.xpos - 1].HP < lowestHP:
            lowestHP = game_map[person.ypos][person.xpos - 1].HP
            xOffset = -1
            yOffset = 0
    if person.xpos + 1 < len(game_map[0]) and isinstance(game_map[person.ypos][person.xpos + 1], Unit) and game_map[person.ypos][person.xpos + 1].type != person.type:
        if game_map[person.ypos][person.xpos + 1].HP < lowestHP:
            lowestHP = game_map[person.ypos][person.xpos + 1].HP
            xOffset = 1
            yOffset = 0
    if person.ypos + 1 < len(game_map) and isinstance(game_map[person.ypos + 1][person.xpos], Unit) and game_map[person.ypos + 1][person.xpos].type != person.type:
        if game_map[person.ypos + 1][person.xpos].HP < lowestHP:
            lowestHP = game_map[person.ypos + 1][person.xpos].HP
            xOffset = 0
            yOffset = 1
    if lowestHP != 300:
        if person.type:
            game_map[person.ypos + yOffset][person.xpos + xOffset].HP -= attack_dmg
        else:
            game_map[person.ypos + yOffset][person.xpos + xOffset].HP -= 3
        if game_map[person.ypos + yOffset][person.xpos + xOffset].HP <= 0:
            if person.type:
                Gob_count -= 1
            else:
                Elf_count -=1
            game_map[person.ypos + yOffset][person.xpos + xOffset] = '.'
        return
    return

def move(person, game_map):
    Q = queue.Queue(0)
    Q.put([[person.xpos, person.ypos]])
    seen = []
    seen.append([person.xpos, person.ypos])
    potential_candidates = []
    while Q.qsize() != 0:
        current_path = Q.get()
        x_pos = current_path[len(current_path) - 1][0]
        y_pos = current_path[len(current_path) - 1][1]
        if near_enemy(person, x_pos, y_pos, game_map) and (person.xpos == x_pos and person.ypos == y_pos):
            return
        elif near_enemy(person, x_pos, y_pos, game_map) and (person.xpos != x_pos or person.ypos != y_pos):
            potential_candidates.append(current_path)
        else:
            if y_pos - 1 >= 0 and game_map[y_pos - 1][x_pos] == "." and [x_pos, y_pos - 1] not in current_path and [x_pos, y_pos - 1] not in seen:
                current_path.append([x_pos, y_pos - 1])
                Q.put(current_path[:])
                current_path = current_path[:len(current_path) - 1]
                seen.append([x_pos, y_pos - 1])
            if x_pos - 1 >= 0 and game_map[y_pos][x_pos - 1] == "." and [x_pos - 1, y_pos] not in current_path and [x_pos - 1, y_pos] not in seen:
                current_path.append([x_pos - 1, y_pos])
                Q.put(current_path[:])
                current_path = current_path[:len(current_path) - 1]
                seen.append([x_pos - 1, y_pos])
            if x_pos + 1 < len(grid[0]) and game_map[y_pos][x_pos + 1] == "." and [x_pos + 1, y_pos] not in current_path and [x_pos + 1, y_pos] not in seen:
                current_path.append([x_pos + 1, y_pos])
                Q.put(current_path[:])
                seen.append([x_pos + 1, y_pos])
                current_path = current_path[:len(current_path) - 1]
            if y_pos + 1 < len(grid) and game_map[y_pos + 1][x_pos] == "." and [x_pos, y_pos + 1] not in current_path and [x_pos, y_pos + 1] not in seen:
                current_path.append([x_pos, y_pos + 1])
                Q.put(current_path[:])
                seen.append([x_pos, y_pos + 1])
                current_path = current_path[:len(current_path) - 1]
    if len(potential_candidates) == 0:
        return
    min_length = 200000
    for i in potential_candidates:
        if len(i) < min_length:
            min_length = len(i)
    paths = []
    for i in potential_candidates:
        if len(i) == min_length:
            paths.append(i)
    chosen = paths[0]
    
    for i in paths:
        if i[len(i) - 1][1] < chosen[len(chosen) - 1][1]:
            chosen = i
        elif i[len(i) - 1][1] == chosen[len(chosen) - 1][1] and i[len(i) - 1][0] < chosen[len(chosen) - 1][0]:
            chosen = i
    game_map[person.ypos][person.xpos] = '.'
    person.xpos = chosen[1][0]
    person.ypos = chosen[1][1]
    game_map[chosen[1][1]][chosen[1][0]] = person
    return

                
def near_enemy(person, X, Y, game_map):
    if X + 1 < len(grid[0]):
        if isinstance(game_map[Y][X + 1], Unit) and game_map[Y][X + 1].type != person.type:
            return True
    if X - 1 >= 0:
        if isinstance(game_map[Y][X - 1], Unit) and game_map[Y][X - 1].type != person.type:
            return True
    if Y + 1 < len(grid):
        if isinstance(game_map[Y + 1][X], Unit) and game_map[Y + 1][X].type != person.type:
            return True
    if Y - 1 >= 0:
        if isinstance(game_map[Y - 1][X], Unit) and game_map[Y  -1][X].type != person.type:
            return True
    return False

def resetHP():
    for i in grid:
        for j in i:
            if isinstance(j, Unit):
                j.HP = 200

def reset_counts():
    global Elf_count
    global orig_elf_count
    Elf_count = orig_elf_count
    global Gob_count
    global orig_gob_count
    Gob_count = orig_gob_count

def update_gob_count(grid):
    ans = 0
    elf_ans = 0
    for i in grid:
        for j in i:
            if isinstance(j, Unit):
                if not j.type:
                    ans+=1
                else: 
                    elf_ans +=1
    global Gob_count
    global Elf_count
    Elf_count = elf_ans
    Gob_count = ans

def part_one(game_map):
    global Elf_count
    global Gob_count
    reset_counts()

    for y, i in enumerate(game_map):
        for x, j in enumerate(i):
            if isinstance(j, Unit):
                j.HP = 200
                j.xpos = x
                j.ypos = y

    count = 0
    Done = False
    while not Done:
        temp = [x[:] for x in game_map]
        for i in game_map:
            for j in i:
                if isinstance(j, Unit):
                    if game_completed() and not Done:
                        count -= 1
                        Done = True
                    move(j, temp)
                    attack(j, temp, 13)
        game_map = [x[:] for x in temp]
        count += 1
    HP_SUM = 0
    for i in game_map:
        for j in i:
            if isinstance(j, Unit):
                if j.HP != -1:
                    HP_SUM += j.HP
    print("PART ONE: ")
    print((HP_SUM) * (count))


def part_two(game_map_input):
    for attack_boost in range(3, 50):
        print(attack_boost)
        game_map = [x[:] for x in game_map_input] 
        global Elf_count
        reset_counts()

        for y, i in enumerate(game_map):
            for x, j in enumerate(i):
                if isinstance(j, Unit):
                    j.HP = 200
                    j.xpos = x
                    j.ypos = y

        count = 0
        Done = False
        while not Done:
            temp = [x[:] for x in game_map]
            for i in game_map:
                for j in i:
                    if isinstance(j, Unit):
                        update_gob_count(temp)
                        if game_completed() and not Done:
                            count -= 1
                            Done = True
                        move(j, temp)
                        attack(j, temp, attack_boost)
            if len(ELVES) != Elf_count:
                Done = False
                break   
            game_map = [x[:] for x in temp]
            count += 1
        if Done:
            HP_SUM = 0
            for i in game_map:
                for j in i:
                    if isinstance(j, Unit):
                        if j.HP != -1:
                            HP_SUM += j.HP
            print("PART TWO: ")
            print((HP_SUM) * (count))
            return

#part_one(grid)
part_two(grid)
