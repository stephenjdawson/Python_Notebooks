"""Blackjack"""
#In VSCode Options, can set shift-enter to send code to terminal OR Jupyter Python interactive window. 

from Blackjack_Packages.Players import Human, Computer
import time

dealer = Computer(0, 0)
player1 = Human(100, 1)

while True:
    print(dealer)
    print(player1)
    player1.clearHand()
    dealer.clearHand()
    while True:
        if player1.bet(input("How much would you like to bet(min. bet = 20)?  ")) == False:
            break
    dealer.hit()
    for _ in range(2):
        player1.hit()
    dealer.showHand()
    player1.showHand()
    if player1.check():
        while True:
            #Need to work on split, double down, and surrender.
            player_turn = input("Please type: 'hit'; 'stay'; 'split'; 'double down'; 'surrender':  ")
            if player_turn.lower() == 'hit':
                player1.hit()
                player1.showHand()
                if player1.check() == False:
                    player1.settleBet()
                    break
                else:
                    continue
            elif player_turn.lower() == 'stay':
                player1.stand()
                player1.showHand()
                player1.check()
                while True:
                    time.sleep(1)
                    dealer.hit()
                    dealer.showHand()
                    if dealer.check() == False:
                        player1.settleBet()
                        break
                    else:
                        continue
                break
    else:
        player1.settleBet()
        