fee = 2

def problem(set):

    if len(set) == 0: return 0
    if len(set) == 1: return 0

    best = 0

    for p in range(len(set)):

        result = solve(set[p], set[p + 1:])
        if result > best:
            best = result


    return best

    pass

def solve(entry, set):

    if len(set) == 0: return 0
    if len(set) == 1: return set[0] - entry - fee

    best = 0
    for i in range(len(set)):

        number = set[i]
        result = number - entry - fee

        new_set = set[i + 1:]
        result_onwards = problem(new_set)

        result = result + result_onwards

        if(result > best):
            best = result

    # print(best)

    return best




# find best combination(s)
print(problem([1,3,2,8,4,10]))
# print(problem([1,3,2,8,2,8,2,9,8,4,10]))