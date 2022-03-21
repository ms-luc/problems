# d is for depth
def problem(set, k,d):

    if len(set) == 0: return 0
    if len(set) == 1: return 1

    best = len(set)

    for ind in range(len(set)):

        result = None

        sum = get_sum(set[:ind])

        if sum <= k:


            remaining_set = set[ind + 1:]
            result = 1 + problem(remaining_set, k, d + 1)

        if result != None and result < best:
            best = result

    return best

def minimize():

    pass

def get_sum(set):

    sum = 0
    for item in set:
        sum = sum + item

    return sum


print(problem([5,1,2,7,3,4], 8, 1))