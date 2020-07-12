first_command = int(input())
second_command = int(input())

american_pie = 1

while american_pie % first_command != 0 or american_pie % second_command !=0:
    american_pie += 1

print(american_pie)