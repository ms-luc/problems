def find_largest_subset(set):

    set.sort()

    works = []

    first = set[0]
    for i in set:

        if i % first != 0 and first % i != 0:

            set1 = set.copy()
            set1.remove(i)

            set2 = set.copy()
            set2.remove(first)

            list1 = find_largest_subset(set1)
            list2 = find_largest_subset(set2)

            if len(list1) > len(list2):
                works = list1
            else:
                works = list2

            break
        else:
            works.append(i)

    return works
    pass

# result = find_largest_subset([3,5,10,20,21])
result = find_largest_subset([6,3,5,9,10,20,21])
print(result)