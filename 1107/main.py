def solution(tree):

    tree_sum = 0
    if isinstance(tree, tuple):

        max_count_1 = 0
        max_count_2 = 0

        for i in tree:

            count1 = solution(i)

            if count1 % 2 == 0 and count1 > max_count_1:
                max_count_1 = count1

            tree_copy = tree.copy()
            tree_copy.remove(i)

            count2 = solution(tree_copy)

            if count2 % 2 == 0 and count2 > max_count_2:
                max_count_2 = count2

        return max_count_1 + max_count_2

    else:
        return 1

    return tree_sum

def getSum(tree):

    count = 0
    for i in tree:

        count = count + 1


    return

print(solution(
    [1,2,[3,[4,6,7,8],5]]
))

