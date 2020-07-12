number_prog = int(input())

if number_prog % 10 == 1 and not number_prog % 100 == 11 or number_prog % 100 == 31 or number_prog % 100 == 51 or number_prog % 100 == 71 or number_prog % 100 == 91:
    print(str(number_prog) + ' программист')

elif number_prog % 100 == 12 or number_prog % 100 == 13 or number_prog % 100 == 14 or number_prog % 100 == 11:
    print(str(number_prog) + ' программистов')

elif number_prog % 10 == 2 or number_prog % 10 == 3 or number_prog % 10 == 4 or number_prog % 100 == 32 or number_prog % 100 == 33 or number_prog % 100 == 34 or number_prog % 100 == 52 or number_prog % 100 == 53 or number_prog % 100 == 54 or number_prog % 100 == 72 or number_prog % 100 == 73 or number_prog % 100 == 74 or number_prog % 100 == 92 or number_prog % 100 == 93 or number_prog % 100 == 94:
    print(str(number_prog) + ' программиста')
else:
    print(str(number_prog) + ' программистов')
