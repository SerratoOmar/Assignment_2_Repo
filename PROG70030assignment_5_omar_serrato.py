# PROG70030 Assignment 5 Omar Serrato
# Blackjack/Twenty One
# 

#NOTE: Program treats the Ace as value 1 only!


import random
import time

results = {}


def draw_cards_1st_turn():
    """Simulates drawing of cards for first turn. Dealer and player."""
    
    
    player_card_1 = draw_card(deck)
    player_card_2 = draw_card(deck)
    player_total = player_card_1.get('value') + player_card_2.get('value') 
    results['player_total'] = player_total
    
    dealer_visible_card = draw_card(deck)
    dealer_hidden_card = draw_card(deck)
    dealer_total = dealer_visible_card.get('value') + dealer_hidden_card.get('value')
    results['dealer_total'] = dealer_total
    results['dealer_card'] = dealer_hidden_card
    
    print(f'\nYou draw a {player_card_1.get("name")} and a {player_card_2.get("name")}. Your total is {player_total}.')
    print(f'The dealer draws a {dealer_visible_card.get("name")} and a hidden card.\n')
    

def hit():
    """Simulates drawing one more card for the player."""
    new_card = draw_card(deck)
    new_total = new_card.get("value") + results['player_total']
    print(f'\nHit! You draw a {new_card.get("name")}, your total is now {new_total}.\n')
    results['player_total'] = new_total    
    
    
def hit_or_stand():
    """Prompts user whether to hit or stand."""
    
    response = input("\nHit or stand? (h/s) \n")
    if response.lower() == 'h':
        hit()
        player_turn()
    elif response.lower() == 's':
        print("\nYou stand.\n")
        time.sleep(1.5)
        print(f"\nThe dealer reveals the hidden card of {results['dealer_card'].get('name')} and has a total of {results['dealer_total']}.\n")
        dealer_turn()
    else:
        print("\nInvalid entry. Try again.\n")
        hit_or_stand()
        
        
    
def dealer_turn():
    
   
    if results['dealer_total'] < 17:
        print("The dealer hits.\n")
        new_card = draw_card(deck)
        new_total = new_card.get('value') + results['dealer_total']
        results['dealer_total'] = new_total
        time.sleep(1.5)
        print(f'The dealer draws a {new_card.get("name")}. Dealer\'s total is now {new_total}.\n')
        if results['dealer_total'] > 21:
            print(f'The Dealer busts! You win!\n\n\n\n')
            #start_game()
        else:
            dealer_turn()
    elif results['dealer_total'] >= 17:
        print("The dealer stands.\n")
        time.sleep(1.5)
        determine_winner()
    

def determine_winner():
    """Determines the winner, by comparing scores."""
    if  results['player_total'] <= results['dealer_total'] and results['dealer_total'] <= 21:
        print(f"Your total is {results['player_total']} and the dealer's total is {results['dealer_total']}. ")
        time.sleep(1.5)
        print("The dealer wins!\n\n\n\n")
        time.sleep(1.5)
    elif results['dealer_total'] < results['player_total'] and results['player_total'] <= 21:
        print(f"Your total is {results['player_total']} and the dealer's total is {results['dealer_total']}. ")
        time.sleep(1.5)
        print("You win!\n\n\n\n")
        time.sleep(1.5)

def player_turn():
    """"""

    if results['player_total'] > 21:
        print(f"You bust! Your total is {results['player_total']}. The dealer wins!\n\n\n\n")
        
    elif results['player_total'] == 21:
        print(f"Your total is {results['player_total']}. You stand.\n")
        time.sleep(1.5)
        print("Dealer turn")
        time.sleep(1.5)
        print(f"\nThe dealer reveals the hidden card of {results['dealer_card'].get('name')} and has a total of {results['dealer_total']}.\n")
        dealer_turn()
        
    elif results['player_total'] < 21:
        print(f"Your total is {results['player_total']}.\n")
        hit_or_stand()        
        

# print('\n')
# print(13*"\u2663""\u2660""\u2665""\u2666")
# print("Welcome to Blackjack.")
# print(50*'-')

def build_standard_deck_dict():
    """Builds a list of dictionaries(cards) to
    represent a deck. Returns the list."""
    new_deck = []
    suits = ["\u2663","\u2660", "\u2665", "\u2666"]
    faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    for face in faces:
        for suit in suits:
            if face <= 10:
                new_card = {'name': str(face) + ' ' + suit, 'value': face}
                new_deck.append(new_card)
            elif face == 11:
                new_card = {'name':'J ' + suit, 'value': 10}
                new_deck.append(new_card)
            elif face == 12:
                new_card = {'name':'Q ' + suit, 'value': 10}
                new_deck.append(new_card)
            elif face == 13:
                new_card = {'name':'K ' + suit, 'value': 10}
                new_deck.append(new_card)
            elif face == 14:
                new_card = {'name':'A ' + suit, 'value': 1}
                new_deck.append(new_card)
    return new_deck
 
def draw_card(deck):
    """Draws a card at random from a deck."""
    
    draw = random.randint(0, (len(deck)-1))
    #print("Card drawn: "+ deck[draw].get('name'))
    drawn_card = deck.pop(draw)
    #print(len(deck))
    return drawn_card
    #drawn_cards.append(drawn_card)   
    


print(13*"\u2663""\u2660""\u2665""\u2666")
print("Welcome to Blackjack.")
print(50*'-')
while True:
    deck = build_standard_deck_dict()    
    #print(len(deck))
    response = input("Would you like to start a new game? y/n: \n")
    if response.lower() == 'y':
        draw_cards_1st_turn()
        player_turn()
    elif response.lower() == 'n':
        print("Goodbye!\n")
        break
    else:
        print("Invalid entry.\n")
        continue


