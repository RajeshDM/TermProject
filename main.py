"""
Christopher Mendez, Rupika Dikkala & Rajesh Mangannavar
Term Project
Blackjack
CS 531 - AI
March 13, 2020
***********************************
"""
import blackjack as b
from pandas import DataFrame

def main():
    game = b.Blackjack(2, 6, 50)
    score = DataFrame(game.play_game()) 
    score.to_csv('FinalScores.csv')

    return


if __name__ == "__main__":
    main()

