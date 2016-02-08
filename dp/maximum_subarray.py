# maximum_subarray.py

# Find the contiguous subarray with the largest product.
# For example, given the array [2,3,-2,4],
# the largest product is 6 for subarray [2,3].

def max_subarray(values):
    if len(values) < 1:
        raise Exception("input must have at least one value")

    local_max = values[0]
    local_min = values[0]
    global_max = values[0]

    for i in xrange(1, len(values)):
        value = values[i]
        current_min = local_min
        current_max = local_max
        local_min = min(value, value*current_min, value*current_max)
        local_max = max(value, value*current_min, value*current_max)
        global_max = max(global_max, local_max)

    return global_max

print max_subarray([2,3,-2,4])

