def smallest_set(X):

    answer = []

    prev = None
    for n in X:

        if prev == None:
            prev = n

        else:
            if n[0] == prev[0] or n[0] == prev[1]:
                answer.append(n[0])
            elif n[1] == prev[0] or n[1] == prev[1]:
                answer.append(n[1])
            else:
                answer.append(n[0])

            prev = None

        pass

    return answer

    pass


answer = smallest_set(
    [(1, 4), (4, 5), (7, 9), (9, 12)]
)

print(answer)
