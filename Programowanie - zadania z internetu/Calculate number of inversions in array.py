def count_inversions(array):

    total = 0
    
    for i in range(0, len(array)):
        for j in range(1, len(array)):
            if array[j - 1] > array[j]:
                x = array[j]
                array[j] = array[j - 1]
                array[j - 1] = x
                total += 1

    return total


