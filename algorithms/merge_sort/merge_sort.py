# merge_sort.py


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


def merge_sort(values):
    if len(values) <= 1:
        return values
    left = merge_sort(values[:len(values)//2])
    right = merge_sort(values[len(values)//2:])
    return merge(left, right)


def main():
    n = int(input())
    values = [int(x) for x in input.split()]
    print(merge_sort(values))


if __name__ == "__main__":
    main()
