


if __name__ == '__main__':
    """
    Calculate the three largest sums of calories

    Read the rows in the file

    if the row is a single newline then reset

    if the row is calories, add it to temp

    if temp is larger than the third largest found so far, then

    sort all four values

    """
    with open("input.txt") as f:

        max_cal = [0, 0, 0]
        temp_sum = 0

        for cals in f:
            cal = int(cals) if cals != '\n' else None

            if cal:
                temp_sum += cal
            else:
                temp_sum = 0

            if temp_sum > max_cal[-1]:
                max_cal = sorted([*max_cal, temp_sum], reverse=True)[:-1]

        print(sum(max_cal))
