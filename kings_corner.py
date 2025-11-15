""" Exercise: Collaborative programming. """

"""Edit by Michael"""
def player_turn(player_hand, play_piles, draw_pile):
    """Process a complete turn for a player in King's Corner.
    
    Args:
        player_hand: List of cards in player's hand
        play_piles: Dictionary of play piles {'A': [], 'B': [], 'C': [], 'D': [], 'K1': [], 'K2': [], 'K3': [], 'K4': []}
        draw_pile: List representing the draw pile
    
    Returns:
        tuple: (updated_player_hand, updated_play_piles, updated_draw_pile, turn_completed)
    """
    turn_completed = False
    if not turn_completed:
        move_type = get_player_move_choice()
        if move_type == "play_card":
            turn_completed = try_play_card(player_hand, play_piles)
        elif move_type == "move_pile":
            turn_completed = try_move_pile(play_piles)
        elif move_type == "draw_card" and draw_pile:
            player_hand.append(draw_pile.pop())
            turn_completed = True
        elif move_type == "end_turn":
            turn_completed = True
    # If still no move completed and draw pile exists, draw a card
    if not turn_completed and draw_pile:
        player_hand.append(draw_pile.pop())
        turn_completed = True
    return player_hand, play_piles, draw_pile, turn_completed

# Mock functions that would be implemented by other group members
def get_player_move_choice():
    """Mock function to get player's move choice"""
    # In final implementation, this would get real user input
    choices = ["play_card", "move_pile", "draw_card", "end_turn"]
    # Simulating player choosing to play a card
    return "play_card"

def try_play_card(player_hand, play_piles):
    """Mock function to attempt playing a card from hand to a pile"""
    # In final implementation, this would handle card placement logic
    if player_hand:  # If player has cards
        card = player_hand.pop(0)  # Remove first card
        # Find an empty king's corner or regular pile to place card
        for pile_name, pile_cards in play_piles.items():
            if not pile_cards:  # Empty pile
                play_piles[pile_name].append(card)
                print(f"Played {card} on pile {pile_name}")
                return True
    return False

def try_move_pile(play_piles):
    """Mock function to attempt moving one pile onto another"""
    # In final implementation, this would validate pile movement rules
    # For now, just simulate a successful move
    print("Moved one pile onto another")
    return True
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
