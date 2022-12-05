import re
# SSCGWJCRB
if __name__ == '__main__':

    stacks = ["" for _ in range(9)]
    with open("input.txt") as f:
        x = f.readlines()[8:0:-1]

    for ix in range(len(x)):
        word = x[ix][1::4]
        for jx, jv in enumerate(word):
            if jv is not " ":
                stacks[jx] += jv

    with open("input.txt") as f:
        for line in f:

            if "move" not in line:
                continue
            nr, fro, to = re.findall(r'\d+', line)

            nr = int(nr)
            fro = int(fro) - 1
            to = int(to) - 1

            stacks[to] += stacks[fro][-nr:]
            stacks[fro] = stacks[fro][:-nr]

    print("".join([stack[-1] for stack in stacks]))
