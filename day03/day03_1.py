from string import ascii_lowercase, ascii_uppercase
letters = list(ascii_lowercase)+list(ascii_uppercase)

if __name__ == '__main__':

    with open("input.txt") as f:

        score = 0

        for hand in f:
            hx = len(hand.strip())
            hand = list(hand[:-1])

            vl, hl = hand[:int(hx/2)], hand[int(hx/2):]
            print(hl, vl)
            letter = list(set(vl).intersection(set(hl)))
            score += letters.index(letter[0])+1
    print(score)
