def problem(set):

    steps = 0
    prev = None
    for item in set:

        if prev == None:
            prev = item
            continue

        while item != prev:

            if item[0] > prev[0] and item[0] > prev[1]:
                prev = edit_tuple(prev, prev[0] + 1, prev[1] + 1)

            elif item[0] < prev[0] and item[0] < prev[1]:
                prev = edit_tuple(prev, prev[0] - 1, prev[1] - 1)

            elif item[0] < prev[0] and item[0] > prev[1]:
                prev = edit_tuple(prev, prev[0] - 1, prev[1] + 1)

            elif item[0] > prev[0] and item[0] < prev[1]:
                prev = edit_tuple(prev, prev[0] + 1, prev[1] - 1)

            elif item[0] > prev[0]:
                prev = edit_tuple(prev, prev[0] + 1, prev[1])

            elif item[0] < prev[0]:
                prev = edit_tuple(prev, prev[0] + 1, prev[1])

            elif item[1] > prev[1]:
                prev = edit_tuple(prev, prev[0], prev[1] + 1)

            elif item[1] < prev[1]:
                prev = edit_tuple(prev, prev[0], prev[1] - 1)

            steps = steps + 1

    return steps

def edit_tuple(tup, item1, item2):

    l = list(tup)
    l[0] = item1
    l[1] = item2
    return tuple(l)



print(problem([(0,0),(1,1),(1,2)]))
