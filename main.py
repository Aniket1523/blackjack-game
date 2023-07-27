import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def compare():
    print(f"User Final Hand {user} Final Score {user_score}")
    print(f"Dealer Final Hand {dealer} Final Score {dealer_score}")
    if user_score > dealer_score:
        print("Winner")
    elif user_score < dealer_score:
        print("Looser")
    elif user_score == dealer_score:
        print("draw")
    print("**************************************************")


def user_play():
    global user_score
    global dealer_score
    user.append(random.choice(cards))
    user_score = sum(user)
    dealer_score = sum(dealer)
    # dealer.append(random.choice(cards))
    print(f"User cards:{user} Total:{user_score} ")
    if user_score == 21:
        print("Winner")
    elif dealer_score == 21:
        print("Looser")
    elif user_score > 21:
        if 11 in user:
            if user_score - 10 > 21:
                print(f"User Final Hand {user} Final Score {user_score}")
                print(f"Dealer Final Hand {dealer} Final Score {dealer_score}")
                print("Looser... You went Over")
            else:
                conti = input("You want to get another card? y or n : ")
                if conti == "y":
                    user_play()
                else:
                    while dealer_score < 17:
                        dealer.append(random.choice(cards))
                        dealer_score = sum(dealer)
                    compare()
        else:
            print(f"User Final Hand {user} Final Score {user_score}")
            print(f"Dealer Final Hand {dealer} Final Score {dealer_score}")
            print("Looser... You went over")
    else:
        conti = input("You want to get another card? y or n : ")
        if conti == "y":
            user_play()
        else:
            print("Dealer playing")
            while dealer_score < 17:
                dealer.append(random.choice(cards))
                dealer_score = sum(dealer)
            compare()


print(logo)
while input("Do you want to play Blackjack game? y or n : ") == 'y':
    user = []
    dealer = []
    user_score = 0
    dealer_score = 0
    user.append(random.choice(cards))
    dealer.append(random.choice(cards))
    print(f"Dealers first card : {dealer}")
    user_play()
