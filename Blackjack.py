import random
from time import sleep

player_score = 0
house_score = 0
while True:

    print('''
     _     _            _    _            _    
    | |   | |          | |  (_)          | |   
    | |__ | | __ _  ___| | ___  __ _  ___| | __
    | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    | |_) | | (_| | (__|   <| | (_| | (__|   < 
    |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
                           _/ |                
                          |__/  
    ''')
    print("Dealer must hit below 17")
    print(f"Player Score: {player_score}, House Score:{house_score}")
    print('''
    **********
    ''')

    wait_seconds = 1
    sleep(wait_seconds)
    #add all cards to a list, including faces
    suit = ["ace", 2,3,4,5,6,7,8,9,10,"jack","queen","king"]
    cards = []
    cards_max_index = 51
    for i in range(4):
        cards.extend(suit)
    #remove a card from the list and add it to player_hand[]
    #do the same for dealer_hand[] and repeat
    player_hand = []
    dealer_hand = []
    for i in range(2):
        player_hand.append(cards.pop(random.randint(0,cards_max_index)))
        cards_max_index -= 1
        dealer_hand.append(cards.pop(random.randint(0,cards_max_index)))
        cards_max_index -= 1


    #display the player_hand and 
    print(f"Player's hand: {player_hand}")
    sleep(wait_seconds)
    print(f"Dealer's hand: [ *, {dealer_hand[1]}]")
    print('''
    **********
    ''')


    hand = []
        #print(cards)
    def add_cards(hand):
        card_number = 0
        p_sum = 0
        card_sum = []
        for card in hand:
            #print(f"Debug: card {card}")
            if isinstance(card, str):
               if card == "ace":
                   card = 11
               else:
                   card = 10
            else:
                card = card
            card_sum.append(card)
        for number in card_sum:
            p_sum += number
        return p_sum


           

            #if 'king' in player_hand:
                #replace king with the number 10


    def ace_detect(hand):
        #Its considered poor practice to use global variables unless necessary. 
        #Whoops. The next line is from ChatGpt and is incorrect on purpose.
        for i in range(len(hand)):
            if hand[i] == "ace":
                    hand[i] = 1
        return hand

    def ace_print(hand):
            #fixed_cards = hand
            #for i in range(len(fixed_cards)):
                #if hand[i] == 1:
                    #hand[i] = "ace"
            #print(f"ace_print debug: {fixed_cards}")
            #return fixed_cards
            return hand

    player_sum = add_cards(player_hand)
    dealer_sum = add_cards(dealer_hand)

    print(f"Player Hand Value: {player_sum}")
    #print(f"Debug: dealer_sum {dealer_sum}")
    #print(f"Debug: Player_sum {player_sum}")
    def blackjack(sum):
        global cards_max_index, player_hand
        if sum > 21:
            player_hand = ace_detect(player_hand)
            print(f"Player Hand: {ace_print(player_hand)}")
            new_sum = add_cards(player_hand)
            print(f"Player Hand Value: {new_sum}")
            if new_sum <= 21:
                return blackjack(new_sum)
            else:
                return sum
        elif sum == 21:
            print("BlackJack!")
            return sum
        else:
            player_choice = str(input("Press 1 to stand, 2 to hit.: "))
            print('''
    **********
    ''')
            if player_choice == "1":
                return sum
            elif player_choice == "2":
                new_card = cards.pop(random.randint(0,cards_max_index))
                sleep(wait_seconds)
                print(f"New Card: {new_card}")
                player_hand.append(new_card)
                if isinstance(new_card, str):
                   if new_card == "ace":
                       new_card = 11
                   else:
                       new_card = 10
                else:
                    new_card = new_card
                new_sum = sum + new_card
                cards_max_index -= 1
                print(f"Player Hand: {ace_print(player_hand)}")
                print(f"Your Hand Value: {new_sum}")
                return blackjack(new_sum)
            else: 
                print("You have been banned.")

    player_result = blackjack(player_sum)
    #print(f"Player Hand Value: {player_result}")
    print('''
    **********
    ''')

    def dealer_blackjack(sum):
        global cards_max_index, dealer_hand
        if sum > player_result and sum < 21:
            return sum
        elif sum > 21:
            dealer_hand = ace_detect(dealer_hand)
            print(f"Dealer Hand: {ace_print(dealer_hand)}")
            new_sum = add_cards(dealer_hand)
            if new_sum <= 21:
                return dealer_blackjack(new_sum)
            else:
                return sum
        elif sum == 21:
            print("Blackjack!")
            return sum
        elif 16 < sum < 21:
            return sum
        else:
            new_card = cards.pop(random.randint(0,cards_max_index))
            sleep(wait_seconds)
            print(f"New Card: {new_card}")
            sleep(wait_seconds)
            dealer_hand.append(new_card)
            if isinstance(new_card, str):
                   if new_card == "ace":
                       new_card = 11
                   else:
                       new_card = 10
            else:
                new_card = new_card
            new_sum = sum + new_card
            cards_max_index -= 1
            sleep(wait_seconds)
            #print(f"Dealer Hand: {dealer_hand}")
            print(f"Dealer Hand: {ace_print(dealer_hand)}")
            return dealer_blackjack(new_sum)
        print(f"Dealer Hand Value: {new_sum}")
    
        print(dealer_hand)
    sleep(wait_seconds)
    if player_result < 21:
        print(f"Dealer Turns Card: {dealer_hand}")
        print('''
    ''')
        dealer_result = dealer_blackjack(dealer_sum)
        print('''
    **********
    ''')
        sleep(wait_seconds)
        print(f"Final Dealer Hand Value: {dealer_result}")
        if player_result > dealer_result and player_result <=21:
            print("Player Wins!")
            player_score += 1
        elif dealer_result > player_result and dealer_result <=21:
            print("House Wins!")
            house_score += 1
        elif dealer_result > 21:
            print("Dealer Bust! Player Wins!")
            player_score += 1
        elif dealer_result == player_result:
            print("Push! House Wins!")
            house_score += 1
    elif player_result > 21:
        print ("Player Bust! House Wins")
        house_score += 1
    else:
        if player_result == 21:
            player_score += 1
        else:
            house_score += 1
    print('''
    **********
    ''')
    print(f"Player Score: {player_score}, House Score:{house_score}")
    sleep(wait_seconds)
    again = input("Press 1 to play again. ")
    if again == "1":
        print('''
    **********
    ''')
        continue
    else:
        break






#CREATE ace_finder function which will subtract 10

#dealer must hit until hitting 17

#To Do:
#black jack is natural only
#keep score


