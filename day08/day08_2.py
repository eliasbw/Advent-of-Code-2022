import numpy as np
from numpy import max
from numpy import max

def str_to_array(text: str):
    with open(text) as f:
        lx = int(len(f.readline().strip()))

    with open(text) as f:
        lx_2 = int(len(f.read()) // lx)

    values = np.zeros((lx_2, lx))
    with open(text) as f:

        for ix, line in enumerate(f.readlines()):
            line = line.strip()

            values[ix] = np.array(list(line), int)

    return values


def view_score(vl, this_height) -> int:
    current_view_height = -1
    view_score = 0

    for rw in vl:
        if rw >= this_height:
            return view_score + 1

        if rw >= current_view_height:
            view_score += 1
            current_view_height = rw

    return max([view_score, 1])


def scorer(rx, cx, values) -> int:
    this = values[rx, cx]

    temp_score = 1

    c = [(3, 2), (1, 2)]

    if rx != len(values) - 1:
        temp_score *= view_score(values[rx+1:, cx], this)
        if (rx, cx) in c:
            print(temp_score, values[rx+1:, cx])

    if rx != 0:
        temp_score *= view_score(values[:rx, cx], this)
        if (rx, cx) in c:
            print(temp_score, values[:rx, cx])

    if cx != len(values[0]) - 1:
        temp_score *= view_score(values[rx, cx+1:], this)
        if (rx, cx) in c:
            print(temp_score)

    if cx != 0:
        temp_score *= view_score(values[rx, :cx], this)
        if (rx, cx) in c:
            print(temp_score)

    return temp_score


if __name__ == "__main__":
    matrix = str_to_array("test.txt")
    print(matrix)

    values = np.zeros(matrix.shape)

    for rx in range(len(matrix)):
        for cx in range(len(matrix[0])):
            values[rx, cx] = scorer(rx, cx, matrix)

    a, b = np.unravel_index(np.argmax(values), values.shape)

    print(3, 2, matrix[3, 2], values[3, 2])
    print(1, 2, matrix[1, 2], values[1, 2])

    print(a, b, values[a, b])
