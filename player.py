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
        self.current_hand_bet = 50
        # give each player an id..?
        self.id = player_id

    # add a card to player hand
    def hit(self,deck):
        while(1):
            card = random.randint(1, 10)
            if deck[card] > 0:
                deck[card] -= 1
                break

        self.hand.append(card)
        #print("current hand: ", self.hand)
        self.memory[card] -= 1
        #print("current memory: ", self.memory)


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
        self.current_hand_bet *= 2
        self.hit(deck)

        return

    # calculate the next decision player should take
    # based on the strategy of AI
    def calculate_decision(self, deck, hand_count, lose_odds):
        prob_decision = {k: hand_count[k] * lose_odds[k] for k in hand_count}
        print("print deicison: ", prob_decision)

        # break the tie between hit/stand by checking the
        # hand count
        if prob_decision["hit"] == prob_decision["stand"]:
            if hand_count["hit"] > hand_count["stand"]:
                self.hit(deck)
            else:
                self.stand()

        # if no ties, pick the best probability
        else:
            decision = max(prob_decision, key=prob_decision.get)
            # pick between hit and double by
            # checking lose probability
            if decision == "hit":
                if lose_odds["hit"] < .49:
                    self.double_down(deck)
                else:
                    self.hit(deck)
            else:
                self.stand()

    def place_bet(self):
        pass


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
    
    def place_bet(self, deck, num_decks):
        if self.balance >= 50 :
            self.current_hand_bet = 50
            self.balance -= self.current_hand_bet
        else:
            self.current_hand_bet = self.balance
            self.balance -= self.current_hand_bet
        pass


class SmartAgent(Player):
    def __init__(self, deck,player_id):
        Player.__init__(self, deck,player_id)
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
            self.balance -= self.current_hand_bet

        if self.current_hand_bet > self.balance:
            self.current_hand_bet = self.balance
            self.balance -= self.current_hand_bet

        print("I will bet", self.current_hand_bet)
        #make bet


class SearchAgent(Player):
    def __init__(self, deck,player_id,number_hands_to_simulate):
        Player.__init__(self, deck,player_id)
        self.runCount = 0
        self.trueCount = 0
        self.number_hands_to_simulate = number_hands_to_simulate

    def calculate_win_odds(self, deck_count, deck, avg_hand, dealer_card):
        print("avg hand", avg_hand, dealer_card)
        total_cards = 52*deck_count
        card_chance = {}
        dealer_hand = {}
        starting_val = dealer_card
        for i in range(1, 11):
            card_chance[i] = (deck[i]/total_cards)

        #print('chance', card_chance[10])
        chance_of_loss = 0
        for j in range(starting_val, 22):
            try:
                dealer_hand[j] = card_chance[j-starting_val]
            except:
                dealer_hand[j] = 0
            if j > avg_hand:
                chance_of_loss += dealer_hand[j]

        print("dealer hand probabilities", total_cards, dealer_hand)
        print("Chance of losing", chance_of_loss)
        return chance_of_loss

    def take_action(self, deck, num_decks, game_state):
        actions = ["hit", "stand"]
        #actions = ["stand"]
        expected_value = {"hit":[] , "stand":[] }
        #simulated_blackjack =
    
        
        for action in actions:
            #print (self.hand)
            for i in range (0,self.number_hands_to_simulate):
                simulated_blackjack = b.SimulatedBlackjack(game_state) 
                simulated_blackjack.copy_state(game_state)
                #for k in range (len(simulated_blackjack.players)):
                #    print ("simulated", simulated_blackjack.players[k].hand)
                #print (self.hand)
                simulated_blackjack.play_simulated_hand(self.id,action)
                for player in simulated_blackjack.players :
                    if player.id == self.id:
                        #print (player.hand)
                        expected_value [action].append(sum(player.hand))
                del simulated_blackjack

        print (expected_value)
        win_odds = {}
        for action in actions : 
            expected_value[action] = (sum(expected_value[action])/len(expected_value[action]))
            # chris calc win-loss odds
            win_odds[action] = self.calculate_win_odds(num_decks, deck, expected_value[action], game_state.dealer.hand[0])

        print("win odds", win_odds)
        #Take win odds and use them to make decision
        #rupika decision making process
        Player.calculate_decision(self, deck, expected_value, win_odds)
        # print (expected_value)

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
            self.balance -= self.current_hand_bet

        if self.current_hand_bet < self.balance:
            self_current_hand_bet = self.balance
            self.balance -= self.current_hand_bet

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
