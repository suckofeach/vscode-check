import random

user_score = 0
comp_score = 0

options = ['rock', 'paper', 'scissors', 'r', 'p', 's', '1', '2', '3']
#            0        1         2        3    4    5    6    7    8


while True:
    user_input = input('type r/p/s: ').lower()
    if user_input == 'stop':
        print('you got %d' %user_score)
        print('computer got %d' %comp_score)
        break
    
    if user_input not in options:
        continue

    random_num = random.randint(0, 2)

    comp_input = options[random_num]

    print('computer said %s.' %comp_input)


    #rock
    if user_input == options[0] or user_input == options[3] or user_input == options[6]:
        if comp_input == options[0]:
            print('pat')
        elif comp_input == options[2]:
            print('you win')
            user_score += 1
        else:
            print('he wins')
            comp_score += 1

    #paper
    if user_input == options[1] or user_input == options[4] or user_input == options[7]:
        if comp_input == options[1]:
            print('pat')
        elif comp_input == options[0]:
            print('you win')
            user_score += 1
        else:
            print('he wins')
            comp_score += 1

    #scissors
    if user_input == options[2] or user_input == options[5] or user_input == options[8]:
        if comp_input == options[2]:
            print('pat')
        elif comp_input == options[1]:
            print('you win')
            user_score += 1
        else:
            print('he wins')
            comp_score += 1
    
    continue