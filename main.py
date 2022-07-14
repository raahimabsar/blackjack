import random
from test import logo

#create a dictionary with cards as keys and their value as values
cards = {"Ace": 11, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 10, "Queen": 10, "King": 10}


def get_card(cards):
    """
    input:
    cards - a dictionary containing the cards as keys

    returns:
    a single card randomly from the cards
    """

    card = random.choice(list(cards.keys()))
    return card

def check_score(deck):
    """
    input:
    deck - a list of computer or user's playing cards

    returns:
    score - an integer after applying the scoring rules of the game
    """

    #initialize score
    score = 0

    #iterate over the cards in the deck and add their scores to score
    for item in deck:
        score += cards[item]

    #set score to 0 if the user or computer has a blackjack
    if score == 21:
        score = 0
        return score
    
    #check if the user or computer had an ace in their deck
    elif score > 21 and "Ace" in deck:
        score -= 10
        return score

    else:
        return score


def compare_score(player_score,comp_score):
    '''
    input:
    player_score -- an integer for user's score
    comp_score -- an integer for computer'score

    returns:
    checks the player_score and comp_score and prints the statement according to
    the blackjack game rules.
    '''
    
    #user or computer wins if they have a blackjack (score = 21)
    if player_score == 0:
        print("You have a blackjack! You win!")
    elif comp_score == 0:
        print("Computer has a blackjack! You loose!")
    
    #check whoever goes over 21 and they loose
    elif player_score > 21:
        print("You went over. You loose")
    elif comp_score > 21:
        print("Opponent went over 21. You win!")
    
    #compare user and computer scores and show the scores with the end result accordingly
    elif player_score == comp_score:
        print(f"Your score is: {player_score}.\nComputer's score is: {comp_score}. That is a tie.")
    elif player_score > comp_score:
        print(f"Your score is: {player_score}.\nComputer's score is: {comp_score}. You Win!")
    else:
        print(f"Your score is: {player_score}.\nComputer's score is: {comp_score}. You loose!")


def blackjack():
 
    #initialize varibales to keep track of user/computer cards and scores
    player_deck = []
    player_score = 0
    comp_deck = []
    comp_score = 0

    #take user input to start the game
    game = input("Do you want to play a game of blackjack? Type y for yes and n for no: ").lower()
    if game == "y":
        print(logo)
        #get cards randomly and append them to user and computer
        player_deck.append(get_card(cards))
        player_deck.append(get_card(cards))
        player_score = check_score(player_deck)

        comp_deck.append(get_card(cards))
        comp_deck.append(get_card(cards))

        #show the user their cards and their current score
        print(f"Your cards are {player_deck}. Your score is: {player_score}")
        print(f"Computer's first card: {comp_deck[0]}")
       
        #ask user to draw more cards
        round2 = input("Do you want to draw another card? Type y for yes and n for no: ")

        #continue the loop as long as the user doesn't have a blackjack or he wishes to exit
        while player_score != 0 and round2 == "y":
                player_deck.append(get_card(cards))
                player_score = check_score(player_deck)
                print(f"Your cards are {player_deck}. Your score is: {player_score}")
                print(f"Computer's first card: {comp_deck[0]}")
                if player_score <= 21:
                    round2 = input("Do you want to draw another card? Type y for yes and n for no: ")
                else:
                    break
        #allow computer to keep drawing cards as long as his score is below user's score
        comp_score = check_score(comp_deck)
        while comp_score < 17:
            comp_deck.append(get_card(cards))
            comp_score = check_score(comp_deck)

        #compare the scores and print results accordingly 
        compare_score(player_score,comp_score)
    else:
        print("Hope you play the next time :(")


blackjack()