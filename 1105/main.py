def solution(lst):

    combinations = all_combinations(lst)

    for comb in combinations:

        for i in range(len(comb)):

            sum1 = sum(comb[i:])
            sum2 = sum(comb[:i])

            if sum1 == sum2:
                return (True, comb[i:], comb[:i])

    return False

def all_combinations(lst):

    if len(lst) == 0: return lst
    if len(lst) == 1: return [lst]

    combinations = []
    for i in range(len(lst)):

        item = lst[i]

        l = lst.copy()
        l.remove(item)

        item = [item]
        l1 = all_combinations(l)

        for i in l1:
            combinations.append( item + i )

    return combinations


# print(solution([1,2,3,4]))
# print(solution([15, 5, 20, 10, 35, 15, 10]))
print(solution([15, 5, 20, 10, 35]))
