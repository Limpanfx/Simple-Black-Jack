import random
import time

print("A simple version of blackjack!")
cards = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King'}
card_values = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

def card_draw():
    card_number = random.randint(1, 13)
    return cards[card_number]

def calculate_hand_value(hand):
    value = sum(card_values[card] for card in hand)
    num_aces = hand.count('Ace')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def is_blackjack(hand):
    return sorted(hand) == ['Ace', 'Ten'] or sorted(hand) == ['Ace', 'Jack'] or sorted(hand) == ['Ace', 'Queen'] or sorted(hand) == ['Ace', 'King']

chips = 100

while chips > 0:
    print(f"\nYou have {chips} chips.")
    bet = int(input("Place your bet: "))
    if bet > chips:
        print("You cannot bet more than you have!")
        continue

    player_hand = [card_draw(), card_draw()]
    dealer_hand = [card_draw(), card_draw()]

    print(f"Your cards: {player_hand} (Total: {calculate_hand_value(player_hand)})")
    print(f"Dealer shows: {dealer_hand[1]}")

    if is_blackjack(player_hand):
        print("Blackjack! You win 1.5x your bet!")
        chips += int(bet * 1.5)
    else:
        while True:
            player_total = calculate_hand_value(player_hand)
            if player_total >= 21:
                break
            action = input("Hit or Stand? (h/s): ")
            if action == 'h':
                player_hand.append(card_draw())
                print(f"Your cards: {player_hand} (Total: {calculate_hand_value(player_hand)})")
            elif action == 's':
                break

        player_total = calculate_hand_value(player_hand)
        if player_total > 21:
            print("You bust! Dealer wins!")
            chips -= bet
        else:
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(card_draw())

            dealer_total = calculate_hand_value(dealer_hand)
            print(f"Dealer's cards: {dealer_hand} (Total: {dealer_total})")

            if dealer_total > 21 or player_total > dealer_total:
                print("You win!")
                chips += bet
            elif dealer_total > player_total:
                print("Dealer wins!")
                chips -= bet
            else:
                print("It's a tie!")

    if chips <= 0:
        print("You have run out of chips. Game over.")
        break
    else:
        play_again = input("Play again? (y/n): ")
        if play_again != 'y':
            break

print(f"Game over. You finished with {chips} chips.")
