from util.inputReader import read_as_strings
import re


def part1and2(my_input):
    count1, count2 = 0, 0
    for s in my_input:
        matches = p.findall(s)[0]
        a, b, c, pwd = matches
        a = int(a)
        b = int(b)

        char_count = pwd.count(c)
        if a <= char_count <= b:
            count1 += 1

        if (pwd[a - 1] == c) != (pwd[b - 1] == c):
            count2 += 1

    print("part1", count1)
    print("part2", count2)


p = re.compile('(\\d+)-(\\d+) (\\w): (\\w+)')

inputs = read_as_strings("../inputs/2020_02.txt")
part1and2(inputs)
