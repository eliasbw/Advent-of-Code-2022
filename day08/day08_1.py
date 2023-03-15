import numpy as np
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


def counter(rx, cx, values) -> bool:

    if rx == 0 or cx == 0 or rx == len(values) - 1 or cx == len(values[0]) - 1:
        return True

    this = values[rx, cx]

    directions = np.min(
        [
            max(values[:rx, cx]),
            max(values[rx, :cx]),
            max(values[rx + 1 :, cx]),
            max(values[rx, cx + 1 :]),
        ]
    )
    if this > directions:
        print(rx, cx, this, directions)

    return this > directions


if __name__ == "__main__":
    score = 0

    matrix = str_to_array("input.txt")
    print(matrix, len(matrix), len(matrix[0]))
    for rx in range(len(matrix)):
        for cx in range(len(matrix[0])):
            score += counter(rx, cx, matrix)

    print(score)
