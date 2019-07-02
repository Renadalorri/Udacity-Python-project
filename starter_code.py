#!/usr/bin/env python3#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return(
        (one == 'rock' and two == 'scissors')or
        (one == 'scissors' and two == 'paper') or
        (one == 'paper' and two == 'rock')
      )


class RandomPlayer(Player):
    def move(self):
        return random.choice(['rock', 'paper', 'scissors'])


class RepeatPlayer(Player):
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    learn_move = 'rock'

    def move(self):
        return self.learn_move

    def learn(self, learn_move, dare_move):
        self.learn_move = dare_move


class CyclerPlayer(Player):
    counter = -1

    def move(self):
        self.counter += 1
        if self.counter == 3:
            self.counter = 0
        return moves[self.counter]


class HumanPlayer(Player):
    def move(self):
        choice = input('rock, paper, scissors? >')

        while choice not in moves:
            print('TRY AGAIN')
            choice = input('rock, paper, scissors? >')
        return (choice)


class Game:
    def __init__(self, p2):
        self.p1 = HumanPlayer()
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"You played {move1}")
        print(f"Opponent played {move2}")
        if beats(move1, move2):
            self.p1.score += 1
            print ("** PLAYER 1 WINS **")
            print(f"Score: Player 1: {move1}  Player 2: {move2}\n")
        elif beats(move2, move1):
            self.p2.score += 1
            print ("** PLAYER 2 WINS **")
            print(f"Score: Player 1: {move1}  Player 2: {move2}\n")
        else:
            print ("**both equal **")

    def play_game(self):
        print("Game start!")
        question = input("how many rounds you would like to play?")
        for round in range(int(question)):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
                print('Player 1 won!')
        elif self.p1.score < self.p2.score:
                print('Player 2 won!')
        else:
                print('The game was a tie!')
                print(
                    'The final score ' + str(self.p1.score) + ' TO ' +
                    str(self.p2.score)
                 )
        print("Game over!")


if __name__ == '__main__':
    ask = input("how would you like to play the game")
    types = ['random', 'repeat', 'reflect', 'cycle']
    while ask not in types:
        ask = input("please try again, enter (random,reflect,cycle,repeat)")
    if ask == 'random':
        game = Game(RandomPlayer())
    elif ask == 'repeat':
        game = Game(Player())
    elif ask == 'reflect':
        game = Game(ReflectPlayer())
    elif ask == 'cycle':
        game = Game(CyclerPlayer())
    game.play_game()
