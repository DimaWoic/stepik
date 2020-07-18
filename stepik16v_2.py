stroke = str(input())

current_letter = 0
next_letter = 1
start = 0
end = 0

while current_letter <= len(stroke) - 1:
    if len(stroke) == 1:
        print(stroke + '1')
        break
    if next_letter == len(stroke) - 1:
        if stroke[next_letter] == stroke[current_letter]:
            print(stroke[current_letter] + str(stroke.count(stroke[current_letter], start)), end='')
        else:
            print(stroke[current_letter] + str(stroke[:next_letter].count(stroke[current_letter])) + stroke[next_letter] + str(stroke.count(stroke[next_letter])), end='')
        break
    if stroke[current_letter] != stroke[next_letter]:
        end = next_letter
        print(stroke[current_letter] + str(stroke.count(stroke[current_letter], start, end)), end='')
        start = current_letter
    current_letter += 1
    next_letter += 1
