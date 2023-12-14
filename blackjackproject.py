import random 


cards = []
suits = ["spades","clubs","hearts","diamonds"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10","j", "Q", "k"]
for suit in suits:
    for rank in ranks:
       cards.append([suit, rank])
def shuffle():
    random.shuffle(cards)   
def deal(number):
    cards_dealt =[]
    for x in range(number):
         card = cards.pop()
         cards_dealt.append(card)
    return cards_dealt

shuffle()
cards_dealt= deal(2)
card = cards_dealt[0]
print(card)