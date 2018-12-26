with open('input.txt') as file:
        inp = file.read().strip().split('\n')

def detect_same_constelation(a, b):
        a = a.split(',')
        b = b.split(',')
        if len(a) == 0 or len(b) == 0:
                return False
        dist = 0
        for i in range(4):
             dist += abs(int(a[i]) - int(b[i]))
        return dist <= 3 and a != b  

related_stars = {}
for a, i in enumerate(inp):
        related_stars[i] = []
        for b, j in enumerate(inp):
                if (detect_same_constelation(i, j)):
                             related_stars[i].append(j)

def recurse(keys, seen):
        if len(keys) == 0: 
                return seen
        if keys[0] not in seen:
                seen.append(keys[0])
                keys += related_stars[keys[0]]
        return recurse(keys[1:], seen)
        
def in_constellations(current_constel, point):
        for i in current_constel:
                if point in i:
                        return True
        return False

constellations = []
for i in related_stars.keys():
        if not in_constellations(constellations, i):
                constellations.append(recurse([i], []))
print(len(constellations))
        