def binary_search(input_array, value):
    # Assume only unique elements
    # Assume array is in increasing order

    # First you must get to the middle of the array
    # Second check whether that middle value is less than the value you are looking for
    # If it less than then search through the left side of the array else check the right

    # Use pointers
    left = 0
    right = len(input_array) - 1

    while left <= right:
        mid = (right + left)/2
        if input_array[mid] == value:
            return mid
        elif value < input_array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
