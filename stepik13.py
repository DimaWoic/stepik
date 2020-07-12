a = int(input())
b = int(input())
c = int(input())
d = int(input())

for column in range(c, d + 1):
    print('\t', column, end='')
print()
for col in range(a, b + 1):
    print(col, '\t', end='')
    for row in range(c, d + 1):
        print(row*col, '\t', end='')
    print()
