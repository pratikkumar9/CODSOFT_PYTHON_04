import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

victories = {
    Action.Rock: [Action.Scissors],
    Action.Scissors: [Action.Paper],
    Action.Paper: [Action.Rock], 
}

# function to take user input
def get_user_choice():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

# function to determine programs action
def get_program_choice():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def determine_winner(user_choice, program_choice):
    defeats = victories[user_choice]
    if user_choice == program_choice:
        print(f"Both players selected {user_choice.name}. It's a tie!")
    elif program_choice in defeats:
        print(f"{user_choice.name} beats {program_choice.name}! You win!")
    else:
        print(f"{program_choice.name} beats {user_choice.name}! You lose.")

while True:
    try:
        user_choice = get_user_choice()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    program_choice = get_program_choice()
    determine_winner(user_choice, program_choice)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break