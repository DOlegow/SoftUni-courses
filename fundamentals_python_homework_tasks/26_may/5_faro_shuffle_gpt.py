def faro_shuffle(deck):
    length = len(deck)
    half = length // 2
    shuffled_deck = []

    for i in range(half):
        shuffled_deck.append(deck[i])
        shuffled_deck.append(deck[i + half])

    return shuffled_deck


cards = input().split()
shuffles = int(input())

for _ in range(shuffles):
    cards = faro_shuffle(cards)

print(cards)
