a = float(input())
b = float(input())
action = input()

if action == 'mod':
    if a == 0 or b == 0:
        print('Деление на 0!')
    else:
        print(a % b)
elif action == 'pow':
    print(a**b)
elif action == 'div':
    if a == 0 or b == 0:
        print('Деление на 0!')
    else:
        print(a // b)
elif action == '/':
    if a == 0 or b == 0:
        print('Деление на 0!')
    else:
        print(a / b)
elif action == '+':
    print(a + b)
elif action == '-':
    print(a - b)
elif action == '*':
    print(a * b)