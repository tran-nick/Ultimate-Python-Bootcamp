from Hand import Hand
from Deck import Deck
from Chips import Chips

def take_bet(player_chips):

    while True:
        
        try:
            player_chips.bet = int(input("Place your bet: "))
            
            if player_chips.bet <= player_chips.total:
                print("Bet was accepted!")
                print()
                break
            else:
                print("Not enough funds")
            
        except:
            print("Please input a numerical value!")


def hit(deck, player):
    
    delt_card = deck.deal()
    player.add_card(delt_card)

    if player.value > 21:
        player.adjust_for_ace()
        

def hit_or_stand(deck,player,dealer):
    

    while True:
        plyr_response = input("Hit or Stand?")

        if plyr_response.lower() == "hit":
            print()
            hit(deck,player)
            show_player(player,dealer)
            print()

        elif plyr_response.lower() == "stand":

            print()
            break

        else:
            print("Not valid choice, please choose again: Hit or Stand?")

def show_some(player,dealer):
    print(player.cards[0] + " & *** ")
    print(dealer.cards[0] + " & *** ")

def show_player(player,dealer):
    print("Player Hand")
    for card in player.cards:
        print(card)

    print()
    print("Dealer Hand")
    print(dealer.cards[0])
    print(" & *** ")
    

def show_all(player,dealer):
    print("Player Hand")
    for card in player.cards:
        print(card)

    print()
    print("Dealer Hand")
    for card in dealer.cards:
        print(card)


# Functions to handle win/lose 
def player_busts(player_chips):
    print("BUST")
    player_chips.lose_bet()

def player_wins(player_chips):
    print("Player wins!")
    player_chips.win_bet()

def dealer_busts(player_chips):
    print("Dealer bust!")
    player_chips.win_bet()

def dealer_wins(player_chips):
    print("Dealer wins!")
    player_chips.lose_bet()

def continue_playing():
    while True:
        player_response = input("Would you like to play again? (Y/N):")

        if player_response.lower() == "n":
            return False
        elif player_response.lower() == "y":
            return True
        else:
            print("Please provide a valid response! (Y/N)")
           
   
while True:
    print("You are now playing blackjack!")
    print()

    #Setting up new deck
    deck = Deck()

    playing = True

    #instantiate player's chip count. Start with 100
    #house doesn't need to track chip count
    player_chips = Chips()


    while playing:

        #need to initialize player hand and chips as two different things,
        #everything new hand is created, new chips is created as well resetting the chip count
        new_player = Hand()
        new_dealer = Hand()

        #deal two cards player / dealer
        new_player.add_card(deck.deal())
        new_player.add_card(deck.deal())

        new_dealer.add_card(deck.deal())
        new_dealer.add_card(deck.deal())

        #Take player bets
        take_bet(player_chips)

        #Show some of the cards
        show_player(new_player,new_dealer)

        hit_or_stand(deck,new_player,new_dealer)


        if new_player.value > 21:

            show_all(new_player,new_dealer)
            player_busts(player_chips)

            break

        #play dealer hand until 17
        while new_dealer.value < 17:

            new_dealer.add_card(deck.deal())

        if new_dealer.value > 21:
        
            show_all(new_player,new_dealer)
            dealer_busts(player_chips)

        elif new_dealer.value < new_player.value:

            show_all(new_player,new_dealer)
            player_wins(player_chips)

        elif new_dealer.value >= new_player.value:

            show_all(new_player,new_dealer)
            dealer_wins(player_chips)


    
        print(f"Your chip balance is: {player_chips.total}")
        print()

        new_game = continue_playing()
        if not new_game:
            break
            
        
    #break while True loop
    break

#End of program
print()
print("Thank you for playing!")

    
            
            
        
        

    



