from random import choice

card_deck = {
    'Ace':(1,11), 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
    'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10
    }

def choose_card():
    """
    Randomly Choose a card
    """
    random_card = choice(list(card_deck.items()))
    return random_card

'''
if __name__ == "__main__":   
    print("__main__")
else:
    print(__name__)
'''
    