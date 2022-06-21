from random import randint

print('Welcome!\nYou need to guess what number computer guessed.')
print('Computer guessed number from 1 to 100')

again = 'y'

while again == 'y':
    player_input = -1
    hidden_number = randint(1, 100)
    while player_input != hidden_number:
        player_input = int(input('\nPlease enter number: '))
        if player_input == hidden_number:
            print('Correct, you win!')
        elif player_input < hidden_number:
            print('Uncorrect, HIGHER!')
        else:
            print('Uncorrect, LOWER!')
    print()
    again = input('Do you want to play again?(y/n): ').lower()

print()
print('Game over!')
input('Press any button...')

