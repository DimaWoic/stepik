a = int(input())
b = int(input())

num = 0
iteration = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        num += i
        iteration += 1

print(num/iteration)
