stroke = str(input())

len_str = len(stroke) - 1

cnt = 1

for s in stroke:
    if len_str <= cnt:
        cnt = 0
        if stroke[::-1][0] == stroke[::-1][1]:
            print(s + str(len(stroke[::-1][0] + stroke[::-1][1])), end='')
        elif stroke[::-1][0] != stroke[::-1][1]:
            print(stroke[::-1][1] + str(stroke[::-1][1].count(stroke[::-1][1])) +  stroke[::-1][0] + str(stroke[::-1][0].count(stroke[::-1][0])))
    elif s == stroke[cnt]:
        cnt += 1
    elif s != stroke[cnt]:
        print(s + str(stroke[:cnt].count(s)), end='')
        cnt += 1
