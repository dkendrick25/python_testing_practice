def is_straight(cards):
    streak = 1
    cards.sort()
    for i in range(1, len(cards)):
        current_card = cards[i]
        previous_card = cards[i - 1]

        if (current_card - previous_card == 1):
            streak = streak + 1

        elif current_card == previous_card:
            pass

        else:
            streak = 1

        if streak == 5:
            return True

    return False
