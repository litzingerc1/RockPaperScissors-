#!/usr/bin/env python3
import random

print("This program plays a game of Rock, Paper, Scissors between"
      " two Players, and reports both Player's scores each round.")

moves = ['rock', 'paper', 'scissors']

# add more  moves to the moves list to make it more interesting
# the Player class is the parent class for all of the Players in this game
# this is the parent player class


class Player():

    def move(self):

        return 'rock'

    def __init__(self):

        self.score = 0
        self.my_move = random.choice(moves)
        self.their_move = random.choice(moves)

    def learn(self, my_move, their_move):

        self.my_move = my_move
        self.their_move = their_move
        return

# class requires a human player to make move selection
# so long as the input is correct via the moves list


class Human_Player(Player):

    def move(self):

        userinput = input('how will you be playing? '
                          ' rock,paper,scissors? '
                          ' type full word:  ').lower()
        if userinput == 'q':
            exit()
        elif userinput in moves:
            return userinput
        else:
            print('Input is incorrect, please re-enter')
            return self.move()  # calling the function

# this player will select a random move


class Random_Player(Player):

    def move(self):

        return random.choice(moves)

# player will cycle through the moves starting with move=rock


class Cycle_Player(Player):

    def move(self):

        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'

# reflects the human player move 1 and move 2


class Reflect_Player(Player):

    def move(self):

        return self.their_move

# function


def beats(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

# start game


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):

        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f'you: {move1}  computer: {move2}')

        if beats(move1, move2):
            self.p1.score = self.p1.score + 1
            print("User one wins!")

        elif beats(move2, move1):
            self.p2.score = self.p2.score + 1
            print("Victory for Computer_Player!")

        else:

            print("Tie game!")
        print(f'scores: you: {self.p1.score} computer: {self.p2.score}')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):

        print("Game start!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        print('\nGame Over!')
        print(f'Scores: You: {self.p1.score} Computer: {self.p2.score}')

        if self.p1.score > self.p2.score:
            print('You Win!!!')
        elif self.p1.score < self.p2.score:
            print('You Lose!')
        else:
            print('No Winners, Tie Game')


def Computer_play():

    gameType = input('Pick computer mode.... random, reflect, or cycle. '
                     'Or press q to quit, '
                     'make sure you write the full word: ').lower()
    if gameType == 'random':
        return Game(Human_Player(), Random_Player())
    elif gameType == 'reflect':
        return Game(Human_Player(), Reflect_Player())
    elif gameType == 'cycle':
        return Game(Human_Player(), Cycle_Player())
    else:
        print('Your input is incorrect, please try again.')
        return gameType()


if __name__ == "__main__":

    game = Computer_play()
    game.play_game()
