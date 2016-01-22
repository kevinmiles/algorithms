def mergesort(input):
    if len(input) <= 1:
        return input
    middle = int(len(input)/2)
    left = mergesort(input[:middle])
    right = mergesort(input[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
