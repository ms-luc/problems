import math


def solution(triplet):

    for i in triplet:

        ab_sqrd = 0
        for a in triplet:

            if i != a:
                ab_sqrd = a * a + ab_sqrd
                ab_sqrd = round(ab_sqrd,2)

        c_sqrd = round(i * i,2)

        print(ab_sqrd)
        print(c_sqrd)
        if ab_sqrd == c_sqrd:
            return True

    return False

print(solution((5, 12, 13)))