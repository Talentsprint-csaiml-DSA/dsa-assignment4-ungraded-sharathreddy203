
def stable_marriage(n, boy_preferences, girl_preferences):
    # Initializing all boys and girls as free
    free_boys = list(range(n))  # Boys who are not yet matched
    engaged = [None] * n         # Engaged pairs for girls
    boy_next_proposal = [0] * n  # Track which girl each boy will propose to next

    # Create a dictionary for quick lookup of girls' preferences (ranked by boys)
    girl_ranking = []
    for preferences in girl_preferences:
        rank = {boy - 1: i for i, boy in enumerate(preferences)}
        girl_ranking.append(rank)
    
    while free_boys:
        # Take the first free boy
        boy = free_boys.pop(0)
        # Get the index of the girl this boy will propose to next
        girl = boy_preferences[boy][boy_next_proposal[boy]] - 1
        boy_next_proposal[boy] += 1

        if engaged[girl] is None:  # If the girl is free, they get engaged
            engaged[girl] = boy
        else:
            current_boy = engaged[girl]
            # Determine if the girl prefers the new boy to her current partner
            if girl_ranking[girl][boy] < girl_ranking[girl][current_boy]:
                # If the girl prefers the new boy, she swaps partners
                engaged[girl] = boy
                free_boys.append(current_boy)  # The current partner becomes free
            else:
                # The girl rejects the new boy, so he remains free
                free_boys.append(boy)

    # Creating the stable pairs list
    matches = [(boy + 1, girl + 1) for girl, boy in enumerate(engaged)]
    return matches
