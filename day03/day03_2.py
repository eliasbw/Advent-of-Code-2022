from string import ascii_lowercase, ascii_uppercase

letters = list(ascii_lowercase) + list(ascii_uppercase)

if __name__ == '__main__':

    with open("input.txt") as f:

        score = 0
        for hand in f:

            hand = hand.strip()
            second_hand = f.readline().strip()
            third_hand = f.readline().strip()

            h1 = set(list(hand))
            h2 = set(list(second_hand))
            h3 = set(list(third_hand))

            letter = list(set(h1).intersection(set(h2)).intersection(set(h3)))
            print(letter)
            score += letters.index(letter[0]) + 1
    print(score)
