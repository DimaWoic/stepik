stroke = 'abc'
cnt = 1
start = 0
end = 0
for s in stroke:
    if len(stroke) == 1:
        print(s + '1', end='')
    elif len(stroke) == stroke.count(s):
        print(s + str(stroke.count(s)), end='')
        break
    if cnt <= len(stroke) - 1:
        if s == stroke[cnt]:
            cnt += 1
        elif s != stroke[cnt]:
            print(s + str(stroke[:cnt].count(s)), end='')
            cnt += 1
    elif cnt == len(stroke) - 2:
        if s == stroke[len(stroke)]:
            cnt += 1
        elif s != stroke[len(stroke)]:
            print(s + str(stroke[:cnt].count(s)), end='')
    elif cnt == len(stroke) - 1:
        if s != stroke[len(stroke)] - 2:
            print(s + str(stroke[len(stroke) - 1].count(s)), end='')
            cnt += 1
        else:
            print(s + str(stroke[:cnt].count(s)), end='')