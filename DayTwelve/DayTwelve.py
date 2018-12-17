NUM_GENERATIONS = 20
offset = 9

with open('input.txt') as file:
        original_pattern = "........." + file.readline()[15:-1]
        rules = file.read().strip().split('\n')
start_pattern = original_pattern
ruleset = {}
for i in rules:
    if i[9:] != ".":
        ruleset[i[0:5]] = i[9:]

for i in range(NUM_GENERATIONS):
    start_pattern += '.........'
    new_pattern = start_pattern
    for j in range(len(new_pattern)):
        if start_pattern[j-2:j+3] in ruleset:
            new_pattern = new_pattern[:j] + '#' + new_pattern[j+1:]
        else:
            new_pattern = new_pattern[:j] + '.' + new_pattern[j+1:]
    start_pattern = new_pattern
    start_pattern = start_pattern.rstrip('.')

ans = 0
for j, i in enumerate(start_pattern):
    if i == '#':
        ans += j - offset
print("PART ONE: ")
print(ans)

start_pattern = original_pattern
previous = ''
count = 0
while True:
    start_pattern += '.........'
    new_pattern = start_pattern
    for j in range(len(new_pattern)):
        if start_pattern[j-2:j+3] in ruleset:
            new_pattern = new_pattern[:j] + '#' + new_pattern[j+1:]
        else:
            new_pattern = new_pattern[:j] + '.' + new_pattern[j+1:]
    start_pattern = new_pattern
    start_pattern = start_pattern.rstrip('.')
    if start_pattern.lstrip('.') == previous:
        sum = 0
        for y, x in enumerate(start_pattern):
            if x == "#":
                sum += y - offset - 1 + 50000000000 - count
        print("DAY TWO: ")
        print(sum)
        break
    count += 1
    previous = start_pattern.lstrip('.')