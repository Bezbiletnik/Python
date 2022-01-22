import random

print('Welcome to the Rock, Paper, Scissors game!')

again = 'y'
dict = {
        0: 'Rock',
        1: 'Paper',
        2: 'Scissors',
    }

while again == 'y':
    player_score, computer_score = 0, 0
    while player_score < 3 and computer_score < 3:
        print()
        try:
            player_input = int(input('Please enter your choice(0-Rock, 1-Paper, 2-Scissors): '))
            if player_input < 0 or player_input > 2:
                raise
        except:
            print('Enter the correct input!')
            continue
        print()
        computer_choice = random.choice(range(3))
        if player_input == computer_choice:
            print(dict[player_input], 'VS', dict[computer_choice])
            print('Draw!', player_score, ':', computer_score)
            continue
        elif (player_input, computer_choice) in [(0,1), (1,2), (2,0)]:
            print(dict[player_input], 'VS', dict[computer_choice])
            computer_score += 1
            print('You lose!', player_score, ':', computer_score)
        else:
            print(dict[player_input], 'VS', dict[computer_choice])
            player_score += 1
            print('You win!', player_score, ':', computer_score)
    print()
    again = input('Do you want to play again?(Y/n): ').lower()

print()
print('Game over!')
input('Push any button...')
