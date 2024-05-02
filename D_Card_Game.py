t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # number of cards
    trump_suit = input()  # trump suit

    card = input()  # card description
    cards = card.split(" ")

    #solution

    cards = sorted(cards, key=lambda x: x[0], reverse=True)
    # print(cards)

    # Rest of the code goes here
    suits = {"C": [], "D": [], "H": [], "S": []}
    for card in cards:
        suits[card[1]].append(card[0])

    # print(suits)
    
    broken = False
    solution = []
    for suit, cards in suits.items():
        if len(cards) > 0:
            if suit == trump_suit:
                continue
            else:
                for _ in range(len(cards) // 2):
                    solution.append([cards.pop() + suit, cards.pop() + suit])
                if len(cards) == 1 and len(suits[trump_suit]) > 0:
                    solution.append([cards.pop() + suit, suits[trump_suit].pop() + trump_suit])
                elif len(cards) == 1 and len(suits[trump_suit]) == 0:
                    broken = True
                    break
    # print(*solution)
    if broken:
        print("IMPOSSIBLE")
        continue

    while len(suits[trump_suit]) >= 2:
        solution.append([suits[trump_suit].pop() + trump_suit, suits[trump_suit].pop() + trump_suit])

    if len(suits[trump_suit]) > 0:
        print("IMPOSSIBLE")
    else:
        for i in range(len(solution)):
            print(" ".join(solution[i]))