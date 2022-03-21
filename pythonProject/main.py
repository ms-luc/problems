def solution(mapping, digit_string):

    if len(digit_string) == 1:
        return mapping[digit_string[0]]

    digit = digit_string[0]
    digit_string = digit_string[1:]

    combinations = []
    for letter in mapping[digit]:
        for i in solution(mapping, digit_string):
            combinations.append( letter + i )

    return combinations



print(solution(
    {
        '2':['a','b','c'],
        '3':['d','e','f']
    },
    '23'
))