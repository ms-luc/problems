def contiguous(numbers, k):

    if len(numbers) == 0: return []

    sum = 0
    answer = []
    result = True

    for i in range(len(numbers)):

        sum = sum + numbers[i]
        answer.append(numbers[i])

        if sum == k:
            break
        if sum > k:
            result = False
            break

    if not result:
        numbers.pop(0)
        answer = contiguous(numbers, k)

    return answer

    pass

# answer = contiguous([1,2,3,4,5], 9)
# answer = contiguous([1,2,3,4,5], 11)
answer = contiguous([10, 2, -2, -20, 10], -10)
print(answer)