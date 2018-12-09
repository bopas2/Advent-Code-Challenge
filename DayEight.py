import string

nodeToChildren = {}
nodeToMetaData = {}
with open('input.txt') as file:
        inp = file.read().strip().split('\n')

for i in inp:
    if i[13] == '0':
        nodeToChildren[i[0]] = ''
    elif i[13] == '1':
        nodeToChildren[i[0]] = i[27]
    elif i[13] == '2':
        nodeToChildren[i[0]] = i[28] + i[31]
    string a = ''
    for l in i[38:]:
        if l != " " and l != ",":
            a += l
    nodeToMetaData[i] = a
