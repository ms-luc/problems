def ghost(set):

    answer = []

    bad_start = []

    index = 0

    for word_i in range(len(set)):

        word_length = len(set[word_i])

        if word_length % 2 != 0:

            if word_length > 1:
                bad_start.append(set[word_i][:-1])
            else:
                bad_start.append(set[word_i])

    for a in range(len(set)):

        word_words = True
        for b in bad_start:

            word_prefix = set[a][:len(b)]
            if word_prefix == b:
                word_words = False

        if word_words:
            answer.append(set[a])

    return answer

    pass

# if ends on uneven remove all words starting with those letters
# print(ghost(['cat', 'calf', 'dog', 'bear']))
print(ghost(['cat', 'calf', 'dog', 'bearer', 'befa']))