if __name__ == "__main__":

    with open("input.txt") as f:
        text = f.readline()

        for ix, letter in enumerate(text):
            if ix == len(text) - 14:
                break

            letters = set(text[ix : ix + 14 : 1])
            if len(letters) == 14:
                print(ix + 14, letters)
                break
