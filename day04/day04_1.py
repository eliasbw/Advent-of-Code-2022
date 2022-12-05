if __name__ == '__main__':
    pairs = 0

    with open("input.txt") as f:


        for hand in f:
            vl, hl = hand.split(",")
            vmin, vmax = vl.split("-")
            hmin, hmax = hl.split("-")

            if int(vmin) <= int(hmin) and int(hmax) <= int(vmax):
                pairs+=1
            elif int(hmin) <= int(vmin) and int(vmax) <= int(hmax):
                pairs+=1
        print(pairs)