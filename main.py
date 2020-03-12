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
    runNum = 0
    #score = 
    #print(score)
   
    #score = DataFrame(game.play_game())
    #for i in range (1, 5):
    game = b.Blackjack(2, 6, 100)
       # print("Game players: " , game.players)
        #print("Game deck: ", game.deck)
        #game.deck[1] -= 2
        #print(game.deck)
        #print("Number of hands to play: ", game.number_hands)
        # game.calculate_win_odds(19, 10)
    score = DataFrame(game.play_game()) 
        #score.append(game.play_game())
    #print("scores", score)
        # game.wrapper_minimax()
    score.to_csv('FinalScores.csv')
    return
    gameScore = DataFrame(score)
    print("Game Score", gameScore)
     
    allScores = []
    for z in (0, 99):
        final_scores = []
        for x in gameScore[z]:
            rows = []
            for y in x:
                rows.append(y)
            final_scores.append(rows)
        #allScores.append(final_scores)

    finalScores = DataFrame(allScores)
    #gameScore.to_csv('ScoreConfig1.csv')
    print('Final scores', finalScores)
    finalScores.to_csv('Final_scores_config1.csv')
    
        #runNum+=1

    return


if __name__ == "__main__":
    main()

