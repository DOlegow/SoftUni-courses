def check_ticket(ticket):
    if len(ticket) != 20:
        return 'invalid ticket'
    first_half = ticket[:10]
    second_half = ticket[10:]
    win_symbols = ['@', '#', '$', '^']
    for ch in win_symbols:
        for j in range(10, 5, -1):
            repetitions = j * ch
            if repetitions in first_half and repetitions in second_half:
                if j == 10:
                    return f'ticket "{ticket}" - {j}{ch} Jackpot!'
                return f'ticket "{ticket}" - {j}{ch}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(', ')]
for ticket in tickets:
    print(check_ticket(ticket))
