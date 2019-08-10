import random


def roll_dice():
    """Roll two dice and return their face   values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1, die2  # Pack die face values into a tuple


def display_dice(dice):
    """Display one roll of the two   dice."""
    die1, die2 = dice
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')


print(roll_dice())
die_values = roll_dice()
display_dice(die_values)

# determine game status and point, based on first roll
sum_of_dice = sum(die_values)

if sum_of_dice in (7, 11):
    game_status = 'WON'
elif sum_of_dice in (2, 3, 12):  # lose
    game_status = 'LOST'
else:  # remember point
    game_status = 'CONTINUE'
    my_point = sum_of_dice
    print('Point is', my_point)

# continue rolling until player wins or loses
while game_status == 'CONTINUE':
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)

    if sum_of_dice == my_point:  # win by making point
        game_status = 'WON'
    elif sum_of_dice == 7:  # lose   by rolling 7
        game_status = 'LOST'

# display "wins” or "loses” message
if game_status == 'WON':
    print('Player wins')
else:
    print('Player loses')

