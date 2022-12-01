


if __name__ == '__main__':

    with open("input.txt") as f:
        max_cal = 0
        temp_sum = 0

        for cals in f:
            cal = int(cals) if cals != '\n' else None

            if cal:
                temp_sum += cal
            else:
                temp_sum = 0

            if temp_sum > max_cal:
                max_cal = temp_sum

        print(max_cal)
