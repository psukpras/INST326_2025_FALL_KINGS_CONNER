""" Exercise: Collaborative programming. """

"""Edit by Michael"""

"""Edit by Phakjira"""
"""Edit by Charlie"""
"""Edit by Attowla"""
def end_round(playerturnhand):
    """
    Args: playerturnhand is a list of tuples displaying the amount of cards
        that display the number and color of each card
    """
    score = 0
    for num, color in playerturnhand:
        if num == 13:
            score += 10
        else:
            score += 1
    return score

def win_condition(p1_score, p2_score):
    """
    Args: p1 and p2 score is the players final score
    """
    if p1_score >= 25:
        print(f"player 2 wins! score:{p2_score}")
    elif p2_score >= 25:
        print(f"player 1 wins! score:{p1_score}")
    else:
        return None

p1 = [(13, "r"), (10, "b"), (8, "r")]
p2 = [(9, "b"), (12, "b"), (3, "r")]

p1_score = end_round(p1)
p2_score = end_round(p2)

print(f"p1 score:{p1_score}")
print(f"p2 score:{p2_score}")

win_condition(p1_score, p2_score) #no winner since only one round was played