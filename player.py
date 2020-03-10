"""
Christopher Mendez, Rupika Dikkala & Rajesh Mangannavar
Term Project
Blackjack
CS 531 - AI
March 13, 2020
***********************************
"""
import random
import blackjack as b

class Player:
    def __init__(self, deck,player_id):
        self.hand = []
        self.memory = deck
        # balance should also be initialized
        self.balance = 500
        #self.start_bet = 0
        #self.current_bet = 0
        self.current_hand_bet = 0
        # give each player an id..?
        self.id = player_id


    def hit(self,deck):
        # pass in card from random card func, for now lets say card = 3
        #card = 3
        #random.randn(13)
        while(1):
            card = random.randint(1, 10)
            if deck[card] > 0:
                deck[card] -= 1
                break
            
            
        
        self.hand.append(card)
        print("current hand: ", self.hand)
        self.memory[card] -= 1
        print("current memory: ", self.memory)


    def reset_hand(self):
        self.hand = []
        
    def initial_bet(self):
        # define minimum bet and pass it in to constructor
        # hardcoding 20 for now
        self.start_bet = 20
        self.current_bet = self.start_bet

    def stand(self):
        pass

    def split(self):
        return

    def double_down(self, deck):
        self.current_bet *= self.current_bet
        self.hit(deck)

        return

    def calculate_minimax(self, action, deck, risk):
        # getting the list of probabilities
        prob = self.get_list()
        reward = [i * self.current_hand_bet for i in prob]
        reward[-1] *= 2

        # prob_reward = list(zip(prob, reward))
        d = ["hit", "stand", "double"]

        prob_decision = dict(zip(d, prob))
        reward_decision = dict(zip(d, reward))

        # if greedy $
        if action == "money":
            decision = max(reward_decision, key=reward_decision.get)
            self.calc_decision(decision, deck)

        # if just wants to win every time
        if action == "win":

            # break the tie between hit/double

            # break the tie between hit/stand

            decision = max(prob_decision, key=prob_decision.get)
            self.calc_decision(decision, deck)


    def calc_decision(self, d, deck):
        if d == "hit":
            self.hit(deck)

        if d == "stand":
            self.stand()

        if d == "double":
            self.double_down(deck)


    def get_list(self):
        return [0.5, 0.3, 0.5]

    def place_bet(self):
        pass

    # def surrender(self):
    #     if not self.played:
    #         # function to remove player from game
    #         # lose half of start bet
    #         self.start_bet /= 2
    #     else:
    #         print("Sorry, you can't surrender after starting the game")

    def take_action(self, deck, num_decks):
        return


class Dealer(Player):
    def __init__(self, deck,player_id):
        Player.__init__(self, deck, player_id)

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
    def __init__(self, deck,player_id):
        Player.__init__(self, deck,player_id)

    def take_action(self, deck, num_decks):
        self.hit(deck)
        print("in override take action")

    def place_bet(self, deck, num_decks):
        if self.balance >= 1 :
            self.current_hand_bet = 1
            self.balance -= self.current_hand_bet
        pass


class SmartAgent(Player):
    def __init__(self, deck,player_id):
        Player.__init__(self, deck,player_id)
        self.runCount = 0
        self.trueCount = 0

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


class SearchAgent(Player):
    def __init__(self, deck,player_id,number_hands_to_simulate):
        Player.__init__(self, deck,player_id)
        self.runCount = 0
        self.trueCount = 0
        self.number_hands_to_simulate = number_hands_to_simulate

    def take_action(self,deck, num_decks, game_state):
        actions = ["hit", "stand"]
        expected_value = {"hit":[] , "stand":[] }
        #rupika decision making process
        #simulated_blackjack = 
    
        for action in actions:
            for i in range (0,self.number_hands_to_simulate):
                simulated_blackjack = b.SimulatedBlackjack(game_state) 
                simulated_blackjack.play_simulated_hand(self.id,action)
                for player in simulated_blackjack.players :
                    if player.id == self.id:
                        #expected_value [action] = (expected_value[action]*(i) + sum(player.hand))/
                        expected_value [action].append(sum(player.hand))


    def take_simulated_action(self,determined_action,simulation_deck):
        if determined_action == "hit":
            getattr(self,determined_action)(simulation_deck)
            return 
        if determined_action == "stand":
            getattr(self,determined_action)()
            return 

    def place_bet(self, deck, num_decks):
        self.update_count(deck, num_decks)
        betting_unit = 25
        self.current_hand_bet = (self.trueCount * betting_unit)
        if( self.current_hand_bet < betting_unit):
            self.current_hand_bet = betting_unit

        print("I will bet", self.current_hand_bet)
        #make bet

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
