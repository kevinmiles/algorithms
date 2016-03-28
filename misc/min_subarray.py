# min_subarray.py

def min_subarray_slow(values):
    result = float('inf')
    for i in xrange(len(values)):
        for j in xrange(i+1, len(values)):
            subarray_sum = sum([values[x] for x in xrange(i,j)])
            result = min(result, subarray_sum)
    return result

def min_subarray_fast(values):
    result = float('inf')
    d = [float('inf') for i in xrange(len(values))]
    for i in xrange(len(values)):
        d[i] = min(values[i], values[i] + d[i-1])
        result = min(result, d[i])
    return result

print min_subarray_slow([1,2,3,4]) # should print 1
print min_subarray_slow([1,-2,3,4]) # should print -2
print min_subarray_slow([1,-2,-3,4]) # should print -5
print min_subarray_fast([]) # should print inf

print min_subarray_fast([1,2,3,4]) # should print 1
print min_subarray_fast([1,-2,3,4]) # should print -2
print min_subarray_fast([1,-2,-3,4]) # should print -5
print min_subarray_fast([]) # should print inf
