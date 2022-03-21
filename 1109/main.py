def solution(x, lst):

    less_than = []
    equal_to = []
    greater_than = []

    for i in lst:

        if i < x:
            less_than.append(i)
        elif i == x:
            equal_to.append(i)
        elif i > x:
            greater_than.append(i)

    result = less_than + equal_to + greater_than
    return result

print(solution(10, [9,12,3,5,14,10,10]))