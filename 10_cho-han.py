import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',4: 'SHI', 5: 'GO', 6: 'ROKU'}

purse = 5000
while True: # Main game loop.
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()   # sys.exit() is used for handling the game's immediate clean exit 
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot) # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the player won:
    roll_is_even = (dice1 + dice2) % 2 == 0
    if roll_is_even:
        correct_bet = 'CHO'
    else:
        correct_bet = 'HAN'
    
    player_won = bet == correct_bet   #evaluates whether a player has won based on their bet (True or False) 

    # Display the bet results:
    if player_won:
        print('You won! You take', pot, 'mon.')
        purse += pot   # Add the pot from player's purse.
        print('The house collects a', pot //10, 'mon fee.')
        purse -= (pot // 10)
    else:
        purse -= pot    # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()    # sys.exit() is used for handling the game's immediate clean exit