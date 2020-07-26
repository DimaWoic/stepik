sum = 0
sqrt = 0

while True:
    num = int(input())
    sum += num
    sqrt += num**2
    if sum == 0:
        break

print(sqrt)