
def permute(array, l, r)

    if len(array) == 0: return []

    item = array.pop()
    return item + print_hi(array)


if __name__ == '__main__':
    print(print_hi([1,2,3]))

