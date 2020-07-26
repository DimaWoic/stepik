stroke = str(input())

a = [int(i) for i in stroke.split()]
sum = 0
for num in a:
    sum +=num

print(sum)
