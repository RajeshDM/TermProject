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
import copy


class Blackjack():
    def __init__(self, number_each_AI, deck_count , number_hands):
        self.players = []   
        
        #for i in range (number_each_AI):  
        #    self.player.append(DumbAgent(deck_count))):
         
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
        self.dealer = p.Dealer(self.deck,0)
        # give player an id here
        self.players.append(p.DumbAgent(self.deck,1))
        #self.players.append(p.DumbAgent(self.deck))
        self.players.append(p.SmartAgent(self.deck,2))
        #self.players.append(p.SearchAgent(self.deck,3,10))
        self.players.append(p.SearchAgent(self.deck,3,10,5))
        pass

    # select a random card from deck
    # will need fine tuning
    def select_card(self):
        card = random.randint(1, 10)
        self.deck[card] -= 1
        return card

    def reset_bank(self):
        for player in self.players :
            player.balance = 5000
        
    def play_game(self):
        #call some kind of bet before the hand
        score = []
        for z in range(0, 50):
            for i in range (self.number_hands):
                self.place_bets()
                self.initial_deal()
                self.play_hand()
                self.dealer.take_action(self.deck)
                score.append(self.distribute_winnings_dealer())
                self.reset_hands()
            self.reset_bank()
            #score.append()
        return score

    def initial_deal(self):
        cards_left = 0
        for i in range (1, 11):
            cards_left += self.deck[i]
            
        print("cards left", cards_left)
        if cards_left < 30:
            print("redealing")
            for i in range(1,11):
                if i < 10:
                    self.deck[i] = 4 * self.deck_count
                elif i == 10:
                    self.deck[i] = 16 * self.deck_count  
        for player in self.players :
            player.hit(self.deck)
            player.hit(self.deck)
        self.dealer.hit(self.deck)


    def place_bets(self):
         for player in self.players :
             if player.id != 3 :
                 player.place_bet(self.deck, self.deck_count)
             else :
                 print ("Placing smart bets")
                 player.place_MCTS_bet(self.deck,self.deck_count,self )

    def play_hand(self):
        for player in self.players :
            
            if player.id != 3 :
                player.take_action(self.deck, self.deck_count)
            else :
                #exit()
                print ("taking search action")
                player.take_action(self.deck,self.deck_count, self)

    def reset_hands(self):
        for player in self.players :
            player.reset_hand()
        self.dealer.reset_hand()

    def wrapper_minimax(self, action="prac", risk=0.31):
        for player in self.players :
            player.calculate_minimax(action, self.deck, risk)


    def distribute_winnings_all(self):
        player_data = {}
        for player in self.players:
            player_data[player] = sum(player.hand)
        player_data[self.dealer] = sum(self.dealer.hand)

        #sort the dictionary
        #decide winnings based on the values

        #player_data.sort()
        round_winner = max(player_data,key=player_data.get)
        
        #round_winner = player_data.pop()
        print ("round winner" , round_winner)
        for player in self.players:
            if round_winner != player :
                round_winner.balance += player.current_hand_bet
                player.balance -= player.current_hand_bet

    def distribute_winnings_dealer(self):
        player_data = {}
        player_data[self.dealer] = sum(self.dealer.hand)
        score = []
        if player_data[self.dealer] > 21:
            player_data[self.dealer] = 0

        for player in self.players:
            player_data[player] = sum(player.hand)
            if player_data[player] > 21:
                player_data[player] = 0
            if player_data[player] > player_data[self.dealer]:
                player.balance += (2*player.current_hand_bet)
                print("player won", player, player.balance, player_data[player], player_data[self.dealer])
                score.append(player.balance)
            elif player_data[player] == player_data[self.dealer]:
                print("player tied", player)
                player.balance += player.current_hand_bet
                score.append(player.balance)
            else:
                print("player lost")
                score.append(player.balance)
        print("score", score)
        return score
                
      
class SimulatedBlackjack(Blackjack):
    def __init__(self, blackjack):
        Blackjack.__init__(self,len(blackjack.players), blackjack.deck_count, 1)


    def play_simulated_hand(self,simulation_player_id, determined_action):
        flag = 0 
        for player in self.players :
            if player.id == simulation_player_id :
                #flag = 1
                #if flag == 1 :
                player.take_simulated_action(determined_action,self.deck)
                #print ("flag 0 - should be here once ")
                flag = 1
                continue
                break
            #if flag == 1 :
            #    print ("flag 1 - should not be here for the time being")
            #    player.take_action()

    def play_simulated_game(self):
        #call some kind of bet before the hand
        score = []
        for z in range(0, 1):
            for i in range (self.number_hands):
                self.initial_deal()
                self.play_hand()
                self.dealer.take_action(self.deck)
                score.append(self.distribute_winnings_dealer())
                self.reset_hands()
            self.reset_bank()
            #score.append()
        return score

    def copy_state(self,blackjack):
        #simulation_blackjack = b.blackjack(2,3,1) 
        #simulation_blackjack = copy.deepcopy(blackjack)
        #for k in range (len(blackjack.players)):
        #    print ("original", blackjack.players[k].hand)
        #self = copy.deepcopy(blackjack)
        self.players = blackjack.players[:]
        for i in range (0,len(blackjack.players)):
            self.players[i] = copy.deepcopy(blackjack.players[i])
        #for k in range (len(self.players)):
        #    print ("self", self.players[k].hand)
        #return simulation_blackjack
