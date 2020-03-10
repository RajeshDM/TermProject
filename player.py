"""
Christopher Mendez, Rupika Dikkala & Rajesh Mangannavar
Term Project
Blackjack
CS 531 - AI
March 13, 2020
***********************************
"""
import random

class Player:
    def __init__(self, deck):
        self.hand = []
        self.memory = deck
        # balance should also be initialized
        self.balance = 500
        #self.start_bet = 0
        #self.current_bet = 0
        self.current_hand_bet = 50
        # give each player an id..?
        self.id = 0

    # add a card to player hand
    def hit(self,deck):
        while(1):
            card = random.randint(1, 10)
            if deck[card] > 0:
                deck[card] -= 1
                break

        self.hand.append(card)
        print("current hand: ", self.hand)
        self.memory[card] -= 1
        print("current memory: ", self.memory)


    # start with fresh hand for new game
    def reset_hand(self):
        self.hand = []

    # bet that the player starts with
    def initial_bet(self):
        # define minimum bet and pass it in to constructor
        # hardcoding 20 for now
        self.start_bet = 20
        self.current_bet = self.start_bet

    # player passes their turn
    def stand(self):
        pass

    # stretch goal lol
    def split(self):
        return

    # player doubles their bet and takes a hit
    # needs a return value?
    def double_down(self, deck):
        self.current_bet *= self.current_bet
        self.hit(deck)

        return

    # calculate the next decision player should take
    # based on the strategy of AI
    def calculate_minimax(self, action, deck, risk):
        print("\n IN THE MINIMAX FUNC")
        # getting the list of probabilities, rajesh code
        # params will probably change
        prob = self.get_list()
        reward = [i * self.current_hand_bet for i in prob]
        reward[-1] *= 2

        d = ["hit", "stand", "double"]
        prob_decision = dict(zip(d, prob))
        reward_decision = dict(zip(d, reward))
        print("this is the reward: ", reward_decision)

        # if AI is greedy and want the most $
        if action == "money":
            decision = max(reward_decision, key=reward_decision.get)
            self.calc_decision(decision, deck)

        # if AI is practical and wants to minimize loss
        if action == "prac":
            # break the tie between hit/double
            if prob_decision["hit"] == prob_decision["double"]:
                if risk > 0.3:
                    self.hit(deck)
                else:
                    self.double_down(deck)

            # break the tie between hit/stand
            if prob_decision["hit"] == prob_decision["stand"]:
                if risk < 0.5:
                    self.hit(deck)
                else:
                    self.stand()

            # no ties, pick the best probability
            else:
                decision = max(prob_decision, key=prob_decision.get)
                self.calc_decision(decision, deck)


    # calc decision helper function
    def calc_decision(self, d, deck):
        if d == "hit":
            self.hit(deck)

        if d == "stand":
            self.stand()

        if d == "double":
            self.double_down(deck)

    # pseudo-code for probability list
    # will be overriden by rajesh code
    def get_list(self):
        return [0.5, 0.3, 0.5]

    def place_bet(self):
        pass


    def take_action(self, deck, num_decks):
        return


class Dealer(Player):
    def __init__(self, deck):
        Player.__init__(self, deck)

    def take_action(self, deck):
        hand_val = 0
        stand_val = 17
        for x in self.hand:
            hand_val += x
        print("hand value", hand_val)
        if hand_val < stand_val:
            self.hit(deck)
        pass
            
        
class DumbAgent(Player):
    def __init__(self, deck):
        Player.__init__(self, deck)

    def take_action(self, deck, num_decks):
        self.hit(deck)
        print("in override take action")

    def place_bet(self, deck, num_decks):
        if self.balance >= 1 :
            self.current_hand_bet = 1
            self.balance -= self.current_hand_bet
        pass


class SmartAgent(Player):
    def __init__(self, deck):
        Player.__init__(self, deck)
        self.runCount = 0
        self.trueCount = 0

    # calculates the number of cards in the deck
    def update_count(self, deck, num_decks):
        num_cards = 0
        self.memory = deck
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
        print(deck)


    def take_action(self, deck, num_decks):
        self.update_count(deck, num_decks)
        hand_val = sum(self.hand)
        stand_val = 17
        print("hand value", hand_val)
        if hand_val < stand_val:
            self.hit(deck)
        pass
        print("Current deck count in action", self.runCount)
        print("Smart agent making play")

    def place_bet(self, deck, num_decks):
        self.update_count(deck, num_decks)
        betting_unit = 25
        self.current_hand_bet = (self.trueCount * betting_unit)
        if( self.current_hand_bet < betting_unit):
            self.current_hand_bet = betting_unit

        print("I will bet", self.current_hand_bet)
        #make bet


