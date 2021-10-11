import random

full_deck = {
    "Two of clubs": 2, "Three of clubs": 3, "Four of clubs": 4, "Five of clubs": 5, "Six of clubs": 6,
    "Seven of clubs": 7, "Eight of clubs": 8, "Nine of clubs": 9, "Ten of clubs": 10,
    "Jack of clubs": 10, "Queen of clubs": 10, "King of clubs": 10, "Ace of clubs": 11,
    "Two of diamonds": 2, "Three of diamonds": 3, "Four of diamonds": 4, "Five of diamonds": 5, "Six of diamonds": 6,
    "Seven of diamonds": 7, "Eight of diamonds": 8, "Nine of diamonds": 9, "Ten of diamonds": 10,
    "Jack of diamonds": 10, "Queen of diamonds": 10, "King of diamonds": 10, "Ace of diamonds": 11,
    "Two of hearts": 2, "Three of hearts": 3, "Four of hearts": 4, "Five of hearts": 5, "Six of hearts": 6,
    "Seven of hearts": 7, "Eight of hearts": 8, "Nine of hearts": 9, "Ten of hearts": 10,
    "Jack of hearts": 10, "Queen of hearts": 10, "King of hearts": 10, "Ace of hearts": 11,
    "Two of spades": 2, "Three of spades": 3, "Four of spades": 4, "Five of spades": 5, "Six of spades": 6,
    "Seven of spades": 7, "Eight of spades": 8, "Nine of spades": 9, "Ten of spades": 10,
    "Jack of spades": 10, "Queen of spades": 10, "King of spades": 10, "Ace of spades": 11,
}


def shuffle_deck():
    deck = list(full_deck.keys())
    random.shuffle(deck)
    return deck


def card_value(card):
    return full_deck[card]


def hand_value(hand):
    total = 0
    for card in hand:
        total += card_value(card)
    return total


def draw_card(hand, deck):
    hand.append(deck.pop(0))


def match_result(hand1, hand2, bet):
    global chips
    if hand_value(hand2) > 21:
        print(f"The dealer busted, you won the game.")
        chips += bet
    elif hand_value(hand1) > hand_value(hand2):
        print(f"Your hand is higher than the dealers hand. You won the game.")
        chips += bet
    elif hand_value(hand1) < hand_value(hand2):
        print(f"Your hand is lower than the dealers hand. You lost the game")
        chips -= bet
    elif hand_value(hand1) == hand_value(hand2):
        print(f"Your hand is equal to the dealers hand. Neither of you won or lost.")


def rematch():
    user_input = str(input("\nWould you like to play again? (Y/N) "))

    if user_input.upper() == "N":
        exit()
    elif user_input.upper() == "Y":
        global game
        game = True
        start_game()


def start_game():
    global chips
    player_hand = []
    dealer_hand = []

    bet = int(input(f"You have {chips} chips. How many would you like to bet? "))

    shuffled_deck = shuffle_deck()
    draw_card(player_hand, shuffled_deck)
    draw_card(dealer_hand, shuffled_deck)
    draw_card(player_hand, shuffled_deck)
    draw_card(dealer_hand, shuffled_deck)

    print(f"You have a {player_hand[0]} and a {player_hand[1]}, with a total of {hand_value(player_hand)} points.")
    print(f"The dealer's visible card is a {dealer_hand[0]}, with a value of {card_value(dealer_hand[0])} points.")

    if hand_value(player_hand) == 21:
        print(f"You got blackjack. You won")
        chips += bet*2
        rematch()

    global game
    while game:
        user_choice = str(input("\nDo you want to Hit or Stand? (H/S) "))

        if user_choice.upper() == "S":
            if hand_value(dealer_hand) < 17:
                print("\nThe dealer draws cards until their hand has a value of 17 or greater.")
                while hand_value(dealer_hand) < 17:
                    draw_card(dealer_hand, shuffled_deck)

            print(f"\nThe deal|ers hand contains the following cards:")
            for card in dealer_hand:
                print(f"- {card}")

            print(f"\nThe dealers hand has a value of {hand_value(dealer_hand)} points.")
            match_result(player_hand, dealer_hand, bet)
            game = False
            rematch()

        elif user_choice.upper() == "H":
            draw_card(player_hand, shuffled_deck)
            print(f"You drew a {player_hand[len(player_hand)-1]}. Yor total is now {hand_value(player_hand)} points.")
            if hand_value(player_hand) > 21:
                print(f"You busted. Game over.")
                chips -= bet
                game = False
                rematch()


chips = 5
game = True
if __name__ == '__main__':
    start_game()
