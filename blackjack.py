"""
Christopher Mendez, Rupika Dikkala & Rajesh Mangannavar
Term Project
Blackjack
CS 531 - AI
March 13, 2020
***********************************
"""
import player as p

class Dealer():
    def _init_ (self):
        self.player = p.player()
    
class blackjack():
    def __init__(self, number_each_AI, deck_count , number_hands):
        self.players = []   
        #for i in range (number_each_AI):  
        #    for j in range(i):
         
        #for key,value in number_each_AI.items():
        #    for i in range (value):
                       
            
        self.dealer = Dealer()
        self.deck = {}
        for i in range(1,11):
            if i < 10:
                self.deck[i] = 4 * deck_count
            elif i == 10:
                self.deck[i] = 16 * deck_count            
        self.number_hands = number_hands
        pass
    
    def play(self):
        self.initial_deal()
        for i in range (self.number_hands):
            self.play_hand()
        pass

    def initial_deal(self):
        
        pass

    def play_hand(self):
        for player in self.players :
            player.take_action()


