import string

def part_two():
    uppercase_characters = string.ascii_uppercase 
    currentTasks = {}

    with open('input.txt') as file:
        inp = file.read().strip().split('\n')

    steps = {}

    for i in inp:
        if i[36] in steps:
            steps[i[36]] = steps[i[36]] + (i[5])
        else:
            steps[i[36]] = i[5]
    
    time = 0
    toSub = []
    while True:
        for i in uppercase_characters:
            if i not in steps and i not in currentTasks:
                currentTasks[i] = 60 - 64 + ord(i)
        tasksToRemove = []
        for j in currentTasks:
            if currentTasks[j] == 0:
                toSub.remove(j)
                uppercase_characters = uppercase_characters[:uppercase_characters.index(j)] + uppercase_characters[uppercase_characters.index(j) + 1:]
                toRemove = []
                for k in steps:
                    if j in steps[k]:
                        steps[k] = steps[k][:steps[k].index(j)] + steps[k][steps[k].index(j) + 1:] 
                    if len(steps[k]) == 0:
                        toRemove.append(k)
                for k in toRemove:
                    steps.pop(k)
                tasksToRemove.append(j)
        for j in tasksToRemove:
            currentTasks.pop(j)
        for i in uppercase_characters:
            if i not in steps and i not in currentTasks:
                currentTasks[i] = 60 - 64 + ord(i)

        time += 1
        for j in (currentTasks):
            if len(toSub) == 5:
                break
            if j not in toSub:
                toSub.append(j)
        
        for j in toSub: 
            currentTasks[j] -= 1

        if not bool(steps) and len(uppercase_characters) == 0:
            break
        print(currentTasks)
    return(time - 1)

def part_one():
    uppercase_characters = string.ascii_uppercase
    orderToReturn = []

    with open('input.txt') as file:
        inp = file.read().strip().split('\n')

    steps = {}

    for i in inp:
        if i[36] in steps:
            steps[i[36]] = steps[i[36]] + (i[5])
        else:
            steps[i[36]] = i[5]
    
    ans = ''
    while True:
        for i in uppercase_characters:
            if i not in steps:
                orderToReturn.append(i)
                ans += i
                uppercase_characters = uppercase_characters[:uppercase_characters.index(i)] + uppercase_characters[uppercase_characters.index(i) + 1:]
                toRemove = []
                for k in steps:
                    if i in steps[k]:
                        steps[k] = steps[k][:steps[k].index(i)] + steps[k][steps[k].index(i) + 1:] 
                    if len(steps[k]) == 0:
                        toRemove.append(k)
                for k in toRemove:
                    steps.pop(k)
        if not bool(steps) and len(uppercase_characters) == 0:
            break
    return ans

print("Order of steps required: " + part_one())
part_two("Time to complete building with 5 workers" + part_two())