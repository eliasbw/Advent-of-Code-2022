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

beat = {
    "X": "Z",
    "Y": "X",
    "Z": "Y"
}

if __name__ == '__main__':

    with open("input.txt") as f:

        score = 0

        for hand in f:
            their, our = hand.split()


            score += our_hand_score.get(our)

            if translate.get(str(their)) == our:
                score += 3

            elif beat.get(translate.get(their)) != our:
                score += 6
    print(score)
