while True:
    try:
        input_read = int(input('how much did you earn last month? '))
        input_count = int(input('how much do you intend to spend on food? '))
        input_count1 = int(input('data nko? '))
        break
    except:
        print("that's not a valid option!")
total_amount = int(input_read)
expense = int(input_count) + int(input_count1)
if expense > total_amount:
    print('not cutting according to size huh? c\'mon now, be serious')
money_left = total_amount - expense
if money_left < 0.5 * total_amount:
    print('hmm boss, ' + str(money_left) + ' left, emiliano rora')
elif money_left > 0.5 * total_amount:
    print('you still have ' + str(money_left) + ', dey ball dey go, sinzuu!!')
input_count2 = input("you'd save right? how much? ")
savings = int(input_count2)
miscellaneous = money_left - savings
if miscellaneous > savings:
    print('still remaining ' + str(miscellaneous))
    input_answer = input("would you like to save more?" + "Y/N ")
    if input_answer == 'Y':
        print('great idea!')
        input_answer1 = input('how much more? ')
        savings1 = savings + int(input_answer1)
        print('use the remaining ' + str(miscellaneous) + " to dey alright, you've earned it!")
    elif input_answer == 'N':
        print('oh well, guess that means you have ' + str(miscellaneous) + ' for miscellaneous expenses')
elif miscellaneous < savings:
    print('use the remaining ' + str(miscellaneous) + " to dey alright, you've earned it!")
