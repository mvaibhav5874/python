def main():
    max_level = int(input("EnterNumberOfLevels> "))
    inc = max_level - 1
    last_index = max_level + inc
    mid_point = int(last_index / 2) + 1

    star = '*'
    space = ' '

    pyramid = []

    for i in range(max_level, 0, -1):
        string = ""
        inc = i - 1
        for j in range(0, last_index):
            if j in range(mid_point - inc - 1, mid_point + inc):
                string += star
            else:
                string += space

        pyramid.append(string)

    pyramid.reverse()
    for line in pyramid:
        print(line)


if __name__ == '__main__':
    main()
