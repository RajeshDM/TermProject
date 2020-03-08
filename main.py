"""
Christopher Mendez, Rupika Dikkala & Rajesh Mangannavar
Term Project
Blackjack
CS 531 - AI
March 13, 2020
***********************************
"""
import blackjack as b

def main():
    game = b.blackjack(2, 3, 5)
    print("Game players: " , game.players)
    print("Game deck: ", game.deck)
    #game.deck[1] -= 2
    #print(game.deck)
    print("Number of hands to play: ", game.number_hands)
    game.calculate_win_odds(19, 10)
    #game.play_game()
    
    return


if __name__ == "__main__":
    main()

