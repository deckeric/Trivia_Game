# Author: Eric Deck
# A trivia game to play based on a csv file of trivia questions.

import csv
import random
import sys


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Question:
    def __init__(self, category, type, difficulty, question, answer1, answer2, answer3, answer4):
        self.category = category
        self.type = type
        self.difficulty = difficulty
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4


players = []
questions = []
line_count = 0


def read_csv(line_count):
    with open('trivia.csv', encoding="utf8", errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            category = row[0]
            type = row[1]
            difficulty = row[2]
            question = row[3]
            answer1 = row[4]
            answer2 = row[5]
            answer3 = row[6]
            answer4 = row[7]
            questions.append(Question(category, type, difficulty, question, answer1, answer2, answer3, answer4))
            line_count += 1
        return line_count


# Create a list of player objects.
def create_players(num_of_players):
    for p in range(1, num_of_players + 1):
        name = input(f"Name of player {p} ")
        players.append(Player(name, 0))


def true_false():
    print(f"True or False:\n{questions[random_num].question}")
    player_answer = input("T or F? ")
    player_answer = player_answer.upper()
    while player_answer != 'T' and player_answer != 'F'and player_answer != 'Q':
        print("That is not a valid input.")
        player_answer = input("\nT or F? ")
        player_answer = player_answer.upper()
    if player_answer == 'T':
        player_answer = 'TRUE'
    elif player_answer == 'F':
        player_answer = 'FALSE'
    else:
        sys.exit()
    if player_answer == questions[random_num].answer1:
        print('Correct!')
        print("-" * 45)
        players[start].score += 1
    else:
        print('Incorrect! You fool!')
        print("-" * 45)


# Multiple Choice
def multiple_choice():
    list = [questions[random_num].answer1, questions[random_num].answer2, questions[random_num].answer3,
            questions[random_num].answer4]
    random.shuffle(list)
    random.shuffle(list)
    random.shuffle(list)
    random.shuffle(list)
    print(f"Multiple Choice:\n{questions[random_num].question}")
    print(f"1. {list[0]}")
    print(f"2. {list[1]}")
    print(f"3. {list[2]}")
    print(f"4. {list[3]}")
    player_answer = input("1, 2, 3, or 4? ")
    player_answer = player_answer.upper()
    while player_answer != '1' and player_answer != '2' and player_answer != '3' and player_answer != '4' and player_answer != 'Q':
        print("That is not a valid input.")
        player_answer = input("1, 2, 3, or 4? ")
    if player_answer == 'Q':
        sys.exit()
    player_answer = int(player_answer)
    if list[player_answer - 1] == questions[random_num].answer1:
        print('Correct!')
        print("-" * 45)
        players[start].score += 1
    else:
        print(f'Incorrect! You fool!\nCORRECT ANSWER: {questions[random_num].answer1}')
        print("-" * 45)


# Main game playing loop. Will loop as long as players choose to play again.
line_count = read_csv(line_count)
game = True
# Loop to continue playing through multiple games
while (game):
    num_of_players = int(input("Hi welcome to Trivia Show. How many players are there? "))
    create_players(num_of_players)
    win = int(input("How many points do you want to play to? "))
    print("Enter 'Q' to quit the game at any point.")
    print("-" * 45)
    playing = True
    # Randomly choose player to begin
    start = random.randint(0, num_of_players - 1)
    # Loop to continue playing the individual game until someone wins.
    while playing:
        # Display scores
        if start > num_of_players - 1:
            start = 0
            print("-" * 45)
            for obj in players:
                print(f'Name: {obj.name} with a Score of: {obj.score}')
            print("-" * 45)
            print("-" * 45)
        print(f"\nAlright {players[start].name} its your turn!\n")
        random_num = random.randint(1, line_count)
        # True/False Question segment
        if questions[random_num].type == 'boolean':
            true_false()
        # Multiple choice question segment
        else:
            multiple_choice()
        start += 1
        # Check if player won game
        for obj in players:
            if obj.score == win:
                print(f"{obj.name} wins!")
                playing = False
    new_game = input("Would you like to play again? Y or N ")
    new_game = new_game.upper()
    while new_game != 'Y' and new_game != 'N':
        print("That is not a valid input.")
        new_game = input("Would you like to play again? Y or N ")
        new_game = new_game.upper()
    if new_game == 'N':
        game = False
    else:
        # Clear list of player objects for new game.
        for obj in players:
            players.pop()
