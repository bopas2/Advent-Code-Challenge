import string

with open('input.txt') as file:
    inp = file.read().strip().split(' ')

sum = 0
def recursive(data):
    global sum
    num_child = int(data.pop(0))
    num_data = int(data.pop(0))
    children = []
    for L in range(num_child):
        children.append(recursive(data))
    meta = []
    for L in range(num_data):
        meta.append(int(data.pop(0)))
        sum += meta[-1]
    return [children, meta]

def recursiveTwo(data):
    sum2 = 0
    if len(data[0]) == 0:
        for i in data[1]:
            sum2 += i
        return sum2
    else:
        for i in data[1]:
            if i <= len(data[0]):
                sum2 += recursiveTwo(data[0][i - 1])
    return sum2

dat = recursive(inp)
print(sum)
print(recursiveTwo(dat))






# ATTEMPT ONE for PART ONE [works for small data input]
# sum = 0
# def recursive(seen, unseen):
#     global sum
#     if len(unseen) == 0:
#         return
#     elif unseen[0] == "0":
#         for i in range(int(unseen[1])):
#             sum += int(unseen[2 + i])
#         ad = []
#         if len(seen) > 0:
#             ad = seen[:-2]
#             ad.append(str(int(seen[-2]) - 1))
#             ad.append(seen[-1])
#         recursive(ad[:-2], ad[-2:] + unseen[2 + int(unseen[1]):])
#     else:
#         recursive(seen + unseen[:2], unseen[2:])


#testing

# recursive(inp)

# def test(data):
#     if len(data) == 0:
#         return
#     data.pop(0)
#     test(data)

# a = "a p p l e s"
# b = a.split(" ")
# print(b)
# test(b)
# print(b)