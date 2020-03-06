"""
Christopher Mendez, Rupika Dikkala & Rajesh Mangannavar
Term Project
Blackjack
CS 531 - AI
March 13, 2020
***********************************
"""


class Player:
    def __init__(self, deck):
        self.hand = []
        self.memory = deck
        self.balance = 0
        self.start_bet = 0
        self.current_bet = 0
        self.played = False

    def hit(self):

        return

    def stand(self):
        return

    def split(self):
        return

    def double_down(self):
        return

    def surrender(self):
        return

    def take_action(self, deck, num_decks):
        return


class DumbAgent(Player):
    def __init__(self, deck):
        Player.__init__(self, deck)

    def take_action(self, deck, num_decks):
        self.hit()
        print("in override take action")   

class SmartAgent(Player):
    def __init__(self, deck):
        Player.__init__(self, deck)
        self.runCount = 0
        self.trueCount = 0

    def update_count(self, deck, num_decks):
        num_cards = 0
        for i in range (1, 11):
            if i < 7 and i > 1:
                self.runCount += (4*num_decks - deck[i])
            elif i == 10:
                self.runCount -= (16*num_decks - deck[i])
            elif i == 1:
                self.runCount -= (4*num_decks - deck[i])
            num_cards += deck[i]
        deck_remain = num_cards/52
        self.trueCount = (self.runCount / deck_remain)
        print("Current deck count", self.runCount)
        print("True count", self.trueCount, num_decks)
        
        
        
    def take_action(self, deck, num_decks):
        self.update_count(deck, num_decks)
        print("Current deck count in action", self.runCount)      
        print("Smart agent making play")

    def place_bet(self, deck, num_decks):
        self.update_count(deck, num_decks)
        betting_unit = 25
        bet = (self.trueCount * betting_unit)
        if( bet < betting_unit):
            bet = betting_unit

        print("I will bet", bet)
        #make bet

    
