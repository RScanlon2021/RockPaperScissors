import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


def rps_game():
    choices = [rock, paper, scissors]
    choices_str = ['rock', 'paper', 'scissors']


    player_choice = input("What do you choose?: " )
    comp_choice_index = random.randint(0,2)
    comp_choice_str = choices_str[comp_choice_index]
    comp_choice = choices[comp_choice_index]

    print(f"You chose {player_choice} ")
    if player_choice == 'rock':
        print(rock)
        print(f"The computer chose {comp_choice_str}{comp_choice} ")
    elif player_choice == 'paper':
        print(paper)
        print(f"The computer chose {comp_choice_str}{comp_choice} ")
    elif player_choice == 'scissors':
        print(scissors)
        print(f"The computer chose {comp_choice_str}{comp_choice} ")
    else:
        print("That's not an option. Please Try again!")

    if player_choice == comp_choice_str:
        print('It is a draw!')
    elif (player_choice == 'rock' and comp_choice == scissors) or \
         (player_choice == 'paper' and comp_choice == rock) or \
         (player_choice == 'scissors' and comp_choice == paper):
        print('YOU WON!!')
    else:
        print('YOU LOSE!!')

rps_game()






