cards = input()
count_of_shuffle = int(input())
deck = cards.split(' ')
for _ in range(count_of_shuffle):
    deck_shuffle = []
    half_deck = int(len(deck) / 2)
    for i in range(half_deck):
        deck_shuffle.append(deck[i])
        deck_shuffle.append(deck[half_deck+i])
    deck = deck_shuffle
print(deck)

