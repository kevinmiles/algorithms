# insertion_sort.py

def insertionsort(input):
    result = []
    for i in range(0, len(input)):
        j = i
        while j > 0 and input[i] < result[j-1]:
            j -= 1
        result.insert(j, input[i])
    return result

