from Blackjack_Packages.Card_Deck import choose_card
"""
Using polymorphism below.
"""
#BUYIN IS NOT WORKING CORRECTLY AFTER REFACTORING, ALSO NEED TO TEST BLACKJACK WIN TO MAKE SURE THE CORRECT WINNINGS ARE BEING DISTRIBUTED

class Players:
    """
    Parent class
    """
    victory_flag = False
    player_value = 0

    # Constructor of the class
    def __init__(self, bank, player):
        self.cards = []
        self.player_bet = 0

        try:
            type(bank) == int
            if bank < 0:
                raise ValueError
        except:
            print("This is not a valid amount")
        else:
            if bank == 0 and player == 0:
                self.bank = "Infinite, I'm the house, bitch!"
            else:
                self.bank = bank

        try: 
            type(player) == int
            if player < 0:
                raise ValueError
        except:
            print("This is not a valid player number.")
        else:
            if player > 0:
                self.player = f"Player {player}"
            else:
                self.player = "Dealer"
     
    def clearHand(self):
        self.cards = []
         
    def hit(self):
        card = choose_card()
        self.cards.append(card) 
    
    def showHand(self):
        print(f"{self.player}'s hand: {self.cards}")
            
    def __str__(self):
        return "%s, Bank: $%s " %(self.player.upper(), self.bank )

class Human(Players):
    """
    Human(bank, player)
    """    
    blackjack_flag = False

    def bet(self, player_bet):
        try:
            self.player_bet = int(player_bet)
            if self.player_bet < 20:
                raise ValueError
            elif self.player_bet > self.bank:
                print("Insufficient funds. Would you like to buy back in?")
                self.buyIn()
        except:
            print("That is not a valid bet.")
            return True
        else:
            self.player_bet = int(player_bet)
            self.bank = self.bank - self.player_bet
            return False

    def check(self):
        summation = 0
        ace_flag = 0
        for card in self.cards:
            if card[0] == "Ace":
                ace_flag += 1
            else:
                summation = summation + card[1]
        while ace_flag > 0:
            if summation + 11 > 21:
                summation = summation + 1
                ace_flag -= 1
            else:
                summation = summation + 11
                ace_flag -= 1
        if summation < 21:
            print(f"{self.player} has: {summation}")
            Players.player_value = summation
            return True
        elif summation > 21:
            print(f"{self.player}: {summation}, you Lose :(")
            del(self.player_bet)
            return False
        else:
            print(f"{self.player}: Blackjack! Winner Winner Chicken Dinner")
            Players.victory_flag = True
            Human.blackjack_flag = True
            return False

    def doubleDown(self):
        pass

    def buyIn(self):
        try:
            self.bank = int(input("How much would you like to buy back in for(min. $20)?"))
            if self.bank < 20:
                raise ValueError
        except:
            print("Insufficient buy-in amount.")
        
    def settleBet(self):
        if Human.blackjack_flag == True:
            self.bank = self.bank + ((self.player_bet*2)*2)
            print(f'{self.player} wins! You now have ${self.bank}')
            del(self.player_bet)
            Human.blackjack_flag = False
        elif Players.victory_flag == True:
            self.bank = self.bank + (self.player_bet*2)
            print(f'{self.player} wins! You now have ${self.bank}')
            del(self.player_bet)
        else:
            return
        Players.victory_flag = False

    def split(self):
        pass  
    
    def stand(self):
        print("Stay")
        return False

    def surrender(self):
        pass

    
class Computer(Players):
    """
    Dealer class
    """
    def check(self):
        summation = 0
        ace_flag = 0
        for card in self.cards:
            if card[0] == "Ace":
                ace_flag += 1
            else:
                summation = summation + card[1]
        while ace_flag > 0:
            if summation + 11 > 21:
                summation = summation + 1
                ace_flag -= 1
            else:
                summation = summation + 11
                ace_flag -= 1
        if summation < 17:
            print(f"{self.player} has: {summation}")
            return True
        elif summation > 21:
            print(f"{self.player}: {summation}, House Loses.")
            Players.victory_flag = True
            return False
        elif summation == 21:
            print(f"{self.player}: House gets Blackjack...")
            return False
        else:
            if summation < Players.player_value:
                Players.victory_flag = True
            else:
                print(f"{self.player}: House wins.")
            return False

'''
if __name__ == "__main__":   
    print("__main__")
else:
    print(__name__)
'''
