# rainwater.py

# Given n non-negative integers representing an elevation map
# where the width of each bar is 1, compute how much water it
# is able to trap after raining.
#
# For example,
# given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#
#     ^
#     |
#   3 |                       +--+
#     |                       |  |
#   2 |          +--+xxxxxxxxx|  +--+xx+--+
#     |          |  |xxxxxxxxx|  |  |xx|  |
#   1 |   +--+xxx|  +--+xxx+--+  |  +--+  +--+
#     |   |  |xxx|  |  |xxx|  |  |  |  |  |  |
#   0 +---+--+---+--+--+---+--+--+--+--+--+--+----->
#       0  1   0  2  1   0  1  3  2  1  2  1
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
# 6 units of rain water (shown with x's) are being trapped.

def rainwater(values):

    # get index of max value
    max_height = 0
    max_index = 0
    for i in xrange(len(values)):
        if values[i] > max_height:
            max_height = values[i]
            max_index = i

    result = 0

    # add up heights from left to max
    prev_high = 0
    for i in xrange(0, max_index, 1):
        prev_high = max(prev_high, values[i])
        result += prev_high - values[i]

    # add up heights from right to max
    prev_high = 0
    for i in xrange(len(values) - 1, max_index, -1):
        prev_high = max(prev_high, values[i])
        result += prev_high - values[i]

    return result

print rainwater([0,1,0,2,1,0,1,3,2,1,2,1])

