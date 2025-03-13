import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def main():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play == "y":
        print(art.logo)
        user_cards, user_score, computer_cards, computer_score = initialize_game()
        cards_and_scores(user_cards, user_score, computer_cards, computer_score)
        winner, computer_cards, computer_score = winner_by_21(
            user_cards, user_score, computer_cards, computer_score)
        while not winner:
            another = input("\nType 'y' to get another card or type 'n' to pass: ").lower()
            if another == "y":
                winner, user_cards, user_score, computer_cards, computer_score = continue_game(
                    user_cards, computer_cards, computer_score)
            elif another == "n":
                winner, user_cards, user_score, computer_cards, computer_score = finish_game(
                    user_cards, user_score, computer_cards, computer_score)
            else:
                winner = False


def finish_game(user_cards, user_score, computer_cards, computer_score):
    computer_cards, computer_score = computer_finish(user_score, computer_cards, computer_score)
    cards_and_scores(user_cards, user_score, computer_cards, computer_score)
    winner, computer_cards, computer_score = winner_by_21(
        user_cards, user_score, computer_cards, computer_score)
    if not winner:
        winner = over_21(user_cards, user_score, computer_cards, computer_score)
        if not winner:
            winner = winner_by_remainder(user_cards, user_score, computer_cards, computer_score)
    return winner, user_cards, user_score, computer_cards, computer_score


def continue_game(user_cards, computer_cards, computer_score):
    user_cards, user_score = draw(user_cards)
    cards_and_scores(user_cards, user_score, computer_cards, computer_score)
    winner, computer_cards, computer_score = winner_by_21(
        user_cards, user_score, computer_cards, computer_score)
    if not winner:
        winner = over_21(user_cards, user_score, computer_cards, computer_score)
    return winner, user_cards, user_score, computer_cards, computer_score


def initialize_game():
    user_cards = []
    user_cards, user_score = draw(user_cards)
    user_cards, user_score = draw(user_cards)
    computer_cards = []
    computer_cards, computer_score = draw(computer_cards)
    return user_cards, user_score, computer_cards, computer_score


def over_21(user_cards, user_score, computer_cards, computer_score):
    if user_score > 21:
        final_hand(user_cards, user_score, computer_cards, computer_score)
        print("\nYou went over 21. Computer wins!!!")
        return True
    elif computer_score > 21:
        final_hand(user_cards, user_score, computer_cards, computer_score)
        print("\nComputer went over 21. You win!!!")
        return True
    else:
        return False


def draw(current_cards):
    current_cards.append(random.choice(cards))
    current_score = sum(current_cards)
    current_cards, current_score = check_ace(current_cards, current_score)
    return current_cards, current_score


def cards_and_scores(user_cards, user_score, computer_cards, computer_score):
    print(f"\nYour cards: {user_cards} - Your score: {user_score}")
    print(f"Computer's cards: {computer_cards} - Computer's score: {computer_score}")


def winner_by_21(user_cards, user_score, computer_cards, computer_score):
    if user_score == 21:
        computer_cards, computer_score = computer_finish(user_score, computer_cards, computer_score)
        winner, computer_cards, computer_score = blackjack(
            user_cards, user_score, computer_cards, computer_score)
        if computer_score == 21 and not winner:
            final_hand(user_cards, user_score, computer_cards, computer_score)
            print("\nIt's a draw")
            return True, computer_cards, computer_score
        elif computer_score != 21 and not winner:
            final_hand(user_cards, user_score, computer_cards, computer_score)
            print("\n21! You win!!!")
            return True, computer_cards, computer_score
        else:
            return True, computer_cards, computer_score
    elif computer_score == 21:
        winner, computer_cards, computer_score = blackjack(
            user_cards, user_score, computer_cards, computer_score)
        if not winner:
            final_hand(user_cards, user_score, computer_cards, computer_score)
            print("\n21! Computer wins!!!")
            return True, computer_cards, computer_score
        else:
            return True, computer_cards, computer_score
    else:
        return False, computer_cards, computer_score


def blackjack(user_cards, user_score, computer_cards, computer_score):
    if {10, 11}.issubset(user_cards) and {10, 11}.issubset(computer_cards):
        final_hand(user_cards, user_score, computer_cards, computer_score)
        print("\nBlackjack tie!!!")
        return True, computer_cards, computer_score
    elif {10, 11}.issubset(user_cards) and computer_score != 21:
        computer_finish(user_score, computer_cards, computer_score)
        final_hand(user_cards, user_score, computer_cards, computer_score)
        print("\nBlackjack! You win!!!")
        return True, computer_cards, computer_score
    elif {10, 11}.issubset(computer_cards) and user_score != 21:
        final_hand(user_cards, user_score, computer_cards, computer_score)
        print("\nBlackjack! Computer wins!!!")
        return True, computer_cards, computer_score
    else:
        return False, computer_cards, computer_score


def winner_by_remainder(user_cards, user_score, computer_cards, computer_score):
    user_remainder = 21 - user_score
    computer_remainder = 21 - computer_score
    if user_remainder < computer_remainder:
        final_hand(user_cards, user_score, computer_cards, computer_score)
        print("\nYou were closer to 21. You win!!!")
        return True
    elif user_remainder > computer_remainder:
        final_hand(user_cards, user_score, computer_cards, computer_score)
        print("\nComputer was closer to 21. Computer wins!!!")
        return True
    elif user_remainder == computer_remainder:
        final_hand(user_cards, user_score, computer_cards, computer_score)
        print("\nIt's a draw")
        return True


def check_ace(current_cards, current_score):
    if current_score > 21:
        if 11 in current_cards:
            index = 0
            for card in current_cards:
                if card == 11:
                    current_cards[index] = 1
                    current_score = sum(current_cards)
                    return current_cards, current_score
                index += 1
        else:
            return current_cards, current_score
    else:
        return current_cards, current_score


def computer_finish(user_score, computer_cards, computer_score):
    if user_score == 21:
        while computer_score < 21:
            computer_cards, computer_score = draw(computer_cards)
    elif computer_score < 21:
        while computer_score < user_score or computer_score < 12:
            computer_cards, computer_score = draw(computer_cards)
    return computer_cards, computer_score


def final_hand(user_cards, user_score, computer_cards, computer_score):
    print(f"\nYour final hand: {user_cards} - Your final score: {user_score}")
    print(f"Computer's final hand: {computer_cards} - Computer's final score: {computer_score}")


while True:
    main()
    print("\n" * 3)
