from numpy import random


def monty_hall(number):
    not_changed = 0
    changed = 0
    for i in range(0, number):
        gift_door = random.choice(['A', 'B', 'C'])  # Randomly choose a door that contains the gift
        user_selection = random.choice(['A', 'B', 'C'])  # represents the random choice of user

        revealed_door = list(set(['A', 'B', 'C']) - set([user_selection, gift_door]))[0]  # the door that host opens after user's selection

        unopened_door = list(set(['A', 'B', 'C']) - set([user_selection, revealed_door]))[0]  # the other door

        if user_selection == gift_door:
            not_changed += 1

        if unopened_door == gift_door:
            changed += 1

    print('Case iterated', number, 'times')
    print('Win case without changing:', (not_changed))
    print('Win case with changing:', (changed))
    print('The chance of winning without changing:', float(((not_changed) / number)))
    print('The chance of winning with changing:', float(((changed) / number)))

monty_hall(3000)







