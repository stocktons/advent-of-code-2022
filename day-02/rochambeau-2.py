from strategy_guide import strategy_guide_key

total_score = 0

with open('data.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        # strip spaces and newlines, turns "A Y\n" into "AY"
        parsed = line.replace(" ", "").strip()

        # parsed looks like: "AY"
        # first letter is rock, paper, or scissors; second letter is lose, draw, or win
        [opponent_gamepiece, game_result] = parsed

        # easier access to the pairs needed to achieve ldw outcomes and score
        ldw_data = strategy_guide_key["ldw"][game_result]

        # look up the number of points for losing, drawing, or winning
        match_points = ldw_data["score"]

        # find which piece to play, and look up its corresponding points
        own_gamepiece = ldw_data[opponent_gamepiece]
        choice_points = strategy_guide_key["rps"][own_gamepiece]

        total_score += match_points + choice_points

print(total_score)