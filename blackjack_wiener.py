###
### Katie Wiener
### Praeses Homework
### Blackjack 
### 4/27/19
###############################

import sys
from random import shuffle

### Global Variables
### Player Stat Array
### win = 0, lose = 1, draw = 2, money =3
player_stat =[0,0,0,1000]


### GV for the Ranks and Suits
ranks = [_ for _ in range (2,11)]+['J', 'Q', 'K', 'A']
suits = ['SPADES', 'HEART', 'DIAMOND', 'CLUB']


### Create Deck
### Function: Creates a single deck of cards
### Input: none
### Returns a new deck of cards
def create_Deck():
    return [[rank, suit] for rank in ranks for suit in suits]


### Card Value
### Fuction: give an int value of a card 
### Input: the card  
### Returns the card value in int
def card_Value(card):
    rank = card[0]

    #Determing value based off of face card
    if rank in ranks[0:-4]:
        return int(rank)
    elif rank is 'A':
        return 11
    else:
        return 10


### Hand Value
### Function: calculates the total sum of hand, whether Ace is 11 or 1, and if player has Blackjack or Busted
### Input: player's hand
### Returns the value in the hand
def hand_Value(hand):
    #Value in hand
    tmpV = sum(card_Value(_) for _ in hand)

    #Number of Aces
    num_aces = len([_ for _ in hand if _[0] is 'A'])

    #Determining whether to have the Ace count as a 1 or 11
    while num_aces > 0:
        if tmpV > 21 and 'A' in ranks:
            tmpV -= 10
            num_aces -= 1
        else:
            break

    #Returning the value of hand while checking for blackjack
    if tmpV < 21:
        return [str(tmpV), tmpV]
    elif tmpV == 21:
        return ['Blackjack!', 21]
    else:
        return ['Bust!', 100]
    

### Game
### Function: runs a game of Blackjakc
### Input: none
### Returns: none
def game():
    player_In = True
    deck = create_Deck()
    shuffle(deck)
    dealer_hand = [deck.pop(), deck.pop()]
    player_hand = [deck.pop(), deck.pop()]
    money = player_stat[3]
    player_bet=0
    bet_In= True

    #Player's action
    while player_In:
        
        if hand_Value (player_hand)[1] == 100:
            break

        #Betting 
        tmp=int(input('Would you like to bet? \n' + 'Yes:[1] No:[0] '))
        if tmp ==0:
            bet_In = False
        if bet_In == True:
            bet = int(input('How much would you like to bet? '))
            player_bet+=bet

        #Printing Hand
        print('\n' + 'Your cards are '+ str(player_hand) + ' for '+ str(hand_Value(player_hand)[0]))
        
        #Playing Game  
        if player_In:
            action = int(input('Would you like to Hit[1] or Stay [2]? '))
            if action == 1:
                
                player_In = True
                new_card = deck.pop()
                print(new_card)
                player_hand.append(new_card)
                print('Dealer dealt a ' + str(new_card))

            else:
                player_In = False
        
    p_score_l, p_score = hand_Value(player_hand)
    d_score_l, d_score = hand_Value(dealer_hand)

    #Dealer's action
    print("Dealer's turn.")
    print('Dealer has '+ str(d_score))
    while hand_Value(dealer_hand)[1] < 17 and p_score !=100 and p_score != 21:
        new_d_card = deck.pop()
        dealer_hand.append(str(new_d_card))
        print('Dealer drew a ' + str(new_d_card))

    #Checking Player's Hand
    if p_score >= 21:
        if p_score == 21:
            print('Blackjack! You win')
            player_stat[3]= money + player_bet
            player_stat[0]+=1
            print('Play again?')
            return

        else:
            print('You busted. Dealer wins.')
            player_stat[1]+=1
            player_stat[3]= money - player_bet
            print('Play again?')
            return 

    #Compairing to dealer's hand
    else:
        if d_score == 100:
            print('Dealer busted. You win!')
            player_stat[0]+=1
        elif d_score == 21:
            print('Dealer got Blackjack. You lose.')
            player_stat[3]= money - player_bet
            player_stat[1]+=1
        elif d_score == p_score:
            print('You tied, no one wins.')
            player_stat[2]+=1
        elif p_score > d_score and p_score != 100:
            print('Your hand is bigger than dealers. You win!')
            player_stat[0]+=1
        else:
            print('Dealer wins with ' + str(d_score))
            player_stat[3]= money - player_bet
            player_stat[1]+=1
            
    print('Play again?')
    return


    

    
### Main
### Function: Main game options 
def main ():
    #Weclome and Selection 
    print('Welcome to Blackjack.')
    print('Menu Selection Options: ')
    print('To play game: 1')
    print('To see current money: 2')
    print('To see player stats: 3')
    print('To quite game: 0')
    
    choice = int(input('Please enter your selection: '))
    while choice != 0:
        #play game
        if choice == 1:
            game() 
        
        #Money
        elif choice == 2:
            print('Current funds: $'+ str(player_stat[3]))

        #Stats
        elif choice == 3:
            print('Current wins: ' + str(player_stat[0]))
            print('Current loses: ' + str(player_stat[1]))
            print('Current draws: ' + str(player_stat[2]))

        #Play again
        print()
        print('##########################')
        print('Menu Selection Options: ')
        print('To play again: 1')
        print('To see current money: 2')
        print('To see player stats: 3')
        print('To quite game: 0')
        choice = int(input('Please enter your selection: '))

    print ('Thank you for playing. Please come back soon.')
    exit()







main (); 
