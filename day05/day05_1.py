import re
# CWMTGHBDW

if __name__ == '__main__':

    with open("input.txt") as f:
        lines = f.readlines()
        x = lines[8:0:-1]

        stacks = ["" for _ in range(9)]
        for word in x:
            for jx, jv in enumerate(word[1::4]):
                if jv is " ":
                    continue
                stacks[jx] += jv

        for line in lines[11:]:
            nr, fro, to = re.findall(r'\d+', line)

            nr = int(nr)
            fro = int(fro) - 1
            to = int(to) - 1

            for ix in range(nr):
                stacks[to] += stacks[fro][-1]
                stacks[fro] = stacks[fro][:-1]

    print("".join([stack[-1] for stack in stacks]))