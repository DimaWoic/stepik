gc = str(input()).lower()

length = 0
cnt_gc = gc.count('g') + gc.count('c')

for i in gc:
    length += 1

percent_rel = cnt_gc/length * 100
print(percent_rel)