VOWELS = set('aeoiuy')
x_set = {'a','p','p','l','e'}
for e in x_set:
    if e in VOWELS:
        print(e)



def sum_neighbors(list1):
    new_list = []
    new_list.append(list1[0] + list1[1])
    x = 1
    while x < len(list1) - 1:
        new_list.append(list1[x - 1] + list1[x] + list1[x + 1])
        x += 1
    new_list.append(list1[x - 1] + list1[x])

    return new_list


print(sum_neighbors(INPUT_LIST))


CONS_LIST = [10, 20, 30, 40, 50]
Count_List = []

for i in CONS_LIST:
    Count_List.append(i)
for i in range(0, len(CONS_LIST)):
    SumList = Count_List[i] + CONS_LIST[i - 1]
    i = i + 1
    print(SumList)

for i in range(0, len(CONS_LIST)):
    if i > 0:
        int(Count_List[i]) + int(CONS_LIST[i - 1])
    elif i < len(CONS_LIST) - 1:
        int(Count_List[i]) + int(CONS_LIST[i + 1])
    else:
        int(CONS_LIST[i])
print(Count_List)

Count_List = [Count_List[i] + CONS_LIST[i - 1] if i > 0 else CONS_LIST[i] for i in range(0, len(CONS_LIST))]
Sum_List = [Count_List[i] + CONS_LIST[i + 1] if (i < len(CONS_LIST) - 1) else CONS_LIST[i] for i in
            range(0, len(CONS_LIST))]
print(Sum_List)
