import random
from test import logo

cards = {"Ace": 11, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 10, "Queen": 10, "King": 10}

def get_card(cards):
    card = random.choice(list(cards.keys()))
    return card

def check_score(deck):
    score = 0
    for item in deck:
        score += cards[item]
    if score == 21:
        score = 0
        return score
    elif score > 21 and "Ace" in deck:
        score -= 10
        return score
    else:
        return score

def compare_score(player_score,comp_score):
    if player_score == 0:
        print("You have a blackjack! You win!")
    elif comp_score == 0:
        print("Computer has a blackjack! You loose!")
    elif player_score > 21:
        print("You went over. You loose")
    elif comp_score > 21:
        print("Opponent went over 21. You win!")
    elif player_score == comp_score:
        print(f"Your score is: {player_score}.\nComputer's score is: {comp_score}. That is a tie.")
    elif player_score > comp_score:
        print(f"Your score is: {player_score}.\nComputer's score is: {comp_score}. You Win!")
    else:
        print(f"Your score is: {player_score}.\nComputer's score is: {comp_score}. You loose!")


def blackjack():
    player_deck = []
    player_score = 0
    comp_deck = []
    comp_score = 0

    game = input("Do you want to play a game of blackjack? Type y for yes and n for no: ").lower()
    if game == "y":
        print(logo)
        player_deck.append(get_card(cards))
        player_deck.append(get_card(cards))
        player_score = check_score(player_deck)

        comp_deck.append(get_card(cards))
        comp_deck.append(get_card(cards))


        print(f"Your cards are {player_deck}. Your score is: {player_score}")
        print(f"Computer's first card: {comp_deck[0]}")
        round2 = input("Do you want to draw another card? Type y for yes and n for no: ")

        while player_score != 0 and round2 == "y":
                player_deck.append(get_card(cards))
                player_score = check_score(player_deck)
                print(f"Your cards are {player_deck}. Your score is: {player_score}")
                print(f"Computer's first card: {comp_deck[0]}")
                if player_score <= 21:
                    round2 = input("Do you want to draw another card? Type y for yes and n for no: ")
                else:
                    break

        comp_score = check_score(comp_deck)
        while comp_score < 17:
            comp_deck.append(get_card(cards))
            comp_score = check_score(comp_deck)

        compare_score(player_score,comp_score)
    else:
        print("Hope you play the next time :(")


blackjack()