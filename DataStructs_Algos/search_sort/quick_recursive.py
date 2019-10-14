def main(array, start, end):
    if start < end:
        part_index = partition(array, start, end)
        main(array, start, part_index-1)
        main(array, part_index+1, end)

    return array


def partition(array, start, end):
    pivot = array[end]
    part_index = start

    for i in range(start, end):
        if array[i] <= pivot:
            array[i], array[part_index] = array[part_index], array[i]
            part_index += 1

    array[part_index], array[end] = array[end], array[part_index]

    return part_index


if __name__ == '__main__':
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print(main(test, 0, len(test)-1))
