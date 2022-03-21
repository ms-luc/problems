def solution(lst):

    floors_with_view = 0

    prev_tallest = 0

    i = len(lst) - 1
    while i >= 0:

        building = lst[i]
        if building > prev_tallest:
            # floors_with_view = floors_with_view + building - prev_tallest
            floors_with_view = floors_with_view + 1
        if prev_tallest < building:
            prev_tallest = building

        i-=1

    return floors_with_view

print(solution([3,7,8,3,6,1]))