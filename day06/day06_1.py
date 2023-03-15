if __name__ == "__main__":

    with open("input.txt") as f:
        text = f.readline()

        for ix, letter in enumerate(text):
            if ix == len(text) - 4:
                break

            letters = {letter, text[ix + 1], text[ix + 2], text[ix + 3]}
            if len(letters) == 4:
                print(ix + 4, letters)
                break
