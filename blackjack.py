"""
Christopher Mendez, Rupika Dikkala & Rajesh Mangannavar
Term Project
Blackjack
CS 531 - AI
March 13, 2020
***********************************
"""
import player as p
import random


class blackjack():
    def __init__(self, number_each_AI, deck_count , number_hands):
        self.players = []   

        #for i in range (number_each_AI):  
        #    for j in range(i):
         
        #for key,value in number_each_AI.items():
        #    for i in range (value):
                       


        self.deck_count = deck_count
        self.deck = {}
        for i in range(1,11):
            if i < 10:
                self.deck[i] = 4 * deck_count
            elif i == 10:
                self.deck[i] = 16 * deck_count            
        self.number_hands = number_hands
        self.dealer = p.Dealer(self.deck)
        # give player an id here
        self.players.append(p.DumbAgent(self.deck))
        self.players.append(p.SmartAgent(self.deck))
        pass

    # select a random card from deck
    # will need fine tuning
    def select_card(self):
        card = random.randint(1, 10)
        self.deck[card] -= 1
        return card

    
    def play(self):
        #call some kind of bet before the hand
        for i in range (self.number_hands):
            self.place_bets()
            self.initial_deal()
            self.play_hand()
            self.dealer.take_action()
            self.distribute_winnings()
        pass

    def initial_deal(self):
        
        pass

    def place_bets(self):
         for player in self.players :
             player.place_bet()

    def play_hand(self):
        for player in self.players :
            player.take_action(self.deck, self.deck_count)

    def distribute_winnings(self):
        player_data = {}
        for player in self.players:
            player_data[player] = sum(player.hand)

        #sort the dictionary
        #decide winnings based on the values


