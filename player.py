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
        # balance should also be initialized
        self.balance = 0
        self.start_bet = 0
        self.current_bet = 0
        # give each player an id..?
        self.id = 0


    def hit(self):
        # pass in card from random card func, for now lets say card = 3
        card = 3
        self.hand.append(card)
        print("current hand: ", self.hand)
        self.memory[card] -= 1
        print("current memory: ", self.memory)



    def initial_bet(self):
        # define minimum bet and pass it in to constructor
        # hardcoding 20 for now
        self.start_bet = 20
        self.current_bet = self.start_bet

    def stand(self):
        pass

    def split(self):
        return

    def double_down(self):
        self.current_bet *= self.current_bet
        self.hit()

        return

    # def surrender(self):
    #     if not self.played:
    #         # function to remove player from game
    #         # lose half of start bet
    #         self.start_bet /= 2
    #     else:
    #         print("Sorry, you can't surrender after starting the game")

    def take_action(self, deck):
        return


class DumbAgent(Player):
    def __init__(self, deck):
        Player.__init__(self, deck)

    def take_action(self, deck):
        self.hit()
        print("\nin override take action")


class SmartAgent(Player):
    def __init__(self, deck):
        Player.__init__(self, deck)
        self.runCount = 0
        self.trueCount = 0

    def update_count(self, deck):
        num_cards = 0
        for i in range (1, 11):
            if i < 7 and i > 1:
                self.runCount += (8 - deck[i])
            elif i == 10:
                self.runCount -= (32 - deck[i])
            elif i == 1:
                self.runCount -= (8 - deck[i])
            num_cards += deck[i]
        num_decks = num_cards/52
        self.trueCount = (self.runCount / num_decks)
        print("Current deck count", self.runCount)
        print("True count", self.trueCount, num_decks)
        print(deck)

    def take_action(self, deck):
        self.update_count(deck)
        print("Current deck count in action", self.runCount)      
        print("Smart agent making play")
