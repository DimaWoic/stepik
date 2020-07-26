stroke = input()

stroke_to_list = [int(i) for i in stroke.split()]
index_m = -1
index_p = +1
if len(stroke_to_list) != 1:
    for num in stroke_to_list:
        if index_p <= len(stroke_to_list) - 1:
            sum = stroke_to_list[index_m] + stroke_to_list[index_p]
            print(str(sum) + ' ', end='')
        index_m += 1
        index_p += 1
    sum = stroke_to_list[len(stroke_to_list)-2] + stroke_to_list[0]
    print(str(sum) + ' ', end='')
else:
    print(str(stroke_to_list[0]) + '', end='')
