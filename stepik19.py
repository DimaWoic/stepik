stroke = input()

list_nums = [int(i) for i in stroke.split()]
list_nums.sort()

b = -1
cnt = 0
if len(list_nums) == 1:
    print(' ', end='')
else:
    tmp_list = []
    for i in list_nums:
        if list_nums.count(i) > 1 and i not in tmp_list:
            tmp_list.append(i)
            print(str(i) + ' ', end='')