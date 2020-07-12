#number_ticket = int(input())

number_ticket = int(input())

first_half = number_ticket // 1000
second_half = number_ticket % 1000
first_half_sum = first_half//100 + first_half % 100//10 + first_half % 100 % 10
second_half_sum = second_half//100 + second_half % 100//10 + second_half % 100 % 10

if first_half_sum == second_half_sum:
    print('Счастливый')
else:
    print('Обычный')