our_hand_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

translate = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

beats = {
    "X": "Z",
    "Y": "X",
    "Z": "Y"
}


if __name__ == '__main__':

    with open("input.txt") as f:

        score = 0

        for hand in f:
            their, tactic = hand.split()

            their = translate.get(their)

            if tactic == "Y":
                our = their
                score += 3

            elif tactic == "Z":
                our = beats.get(beats.get(their))
                score += 6

            else:
                our = beats.get(their)

            score += our_hand_score.get(our)

    print(score)
    # 11618
