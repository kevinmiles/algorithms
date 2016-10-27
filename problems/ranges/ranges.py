
def merge_ranges(ranges, new_range):
    ranges.append(new_range)
    ranges.sort()
    for i in xrange(len(ranges)):
        range = ranges[i]
        if new_range[0] <= range[1]:
            ranges[i] = (range[0], max(new_range[1], range[1]))
    i = 0
    while i < len(ranges) - 1:
        cur_range = ranges[i]
        next_range = ranges[i+1]
        if cur_range[1] >= next_range[0]:
            ranges[i] = (min(cur_range[0], next_range[0]), max(cur_range[1], next_range[1]))
            del ranges[i+1]
        else:
            i += 1
    return ranges

assert merge_ranges([(1,2), (4,5), (7,8)], (2,3)) == [(1, 3), (4, 5), (7, 8)]
assert merge_ranges([(1,2), (4,5), (7,8)], (3,4)) == [(1, 2), (3, 5), (7, 8)]
assert merge_ranges([(1,2), (4,6)], (3,8)) == [(1, 2), (3, 8)]
print merge_ranges([(1,2), (4,6)], (2,8))
assert merge_ranges([(1,2), (4,6)], (2,8)) == [(1, 8)]
print merge_ranges([(1,2), (3,4), (5,10)], (1,10))
assert merge_ranges([(1,2), (3,4), (5,10)], (1,10)) == [(1, 10)]
print merge_ranges([(1,2), (9,10)], (5,6))
assert merge_ranges([(1,2), (9,10)], (5,6)) == [(1,2), (5,6), (9,10)]
