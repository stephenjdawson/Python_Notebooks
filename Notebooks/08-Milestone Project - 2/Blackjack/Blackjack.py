"""Blackjack"""
#In VSCode Options, can set shift-enter to send code to terminal OR Jupyter Python interactive window. 

from Blackjack_Packages.Players import Human, Computer

dealer = Computer(0, 0)
player1 = Human(100, 1)

while True:
    print(dealer)
    print(player1)
    player1.clearHand()
    dealer.clearHand()
    player1.bet(input("How much would you like to bet(min. bet = 20)?  "))
    dealer.hit()
    for _ in range(2):
        player1.hit()
    dealer.showHand()
    player1.showHand()
    player1.check()
    while True:
        player_turn = input("Please type: 'hit'; 'stay'; 'split'; 'double down'; 'surrender':  ")
        if player_turn.lower() == 'hit':
            player1.hit()
            player1.showHand()
            if player1.check() == False:
                break
            else:
                continue
        elif player_turn.lower() == 'stay':
            player1.stand()
            player1.showHand()
            while True:
                dealer.hit()
                dealer.showHand()
                if dealer.check() == False:
                    break
                else:
                    continue
            break
        