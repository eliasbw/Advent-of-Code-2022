if __name__ == '__main__':
    pairs = 0

    with open("input.txt") as f:

        for hand in f:
            vl, hl = hand.split(",")
            vmin, vmax = vl.split("-")
            hmin, hmax = hl.split("-")

            vl = set(list(range(int(vmin), int(vmax) + 1)))
            hl = set(list(range(int(hmin), int(hmax) + 1)))
            if vl.intersection(hl):
                pairs += 1
        print(pairs)
