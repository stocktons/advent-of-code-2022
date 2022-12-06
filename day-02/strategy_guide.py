strategy_guide_key = {
    # values for rock(A), paper(B), scissors(C) 
    "rps": {"A": 1, "B": 2, "C": 3}, 
    # lose(x), draw(y), and win(z) combos and their values
    "ldw": {
        "X": {"A": "C", "B": "A", "C": "B", "score": 0}, 
        "Y": {"A": "A", "B": "B", "C": "C", "score": 3}, 
        "Z": {"A": "B", "B": "C", "C": "A", "score": 6}, 
    }
}