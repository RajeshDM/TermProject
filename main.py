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
    game = b.Blackjack(2, 6, 500)
    print("Game players: " , game.players)
    print("Game deck: ", game.deck)
    #game.deck[1] -= 2
    #print(game.deck)
    print("Number of hands to play: ", game.number_hands)
    # game.calculate_win_odds(19, 10)
    score = game.play_game()
    print("Game Score", score)
    # game.wrapper_minimax()

    gameScore = DataFrame(score)
    gameScore.to_csv('scores.csv')

    return


if __name__ == "__main__":
    main()

