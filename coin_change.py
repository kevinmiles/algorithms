# coin_change.py

# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that
# amount. If that amount of money cannot be made up by any combination of the coins,
# return -1.
#
# Example 1:
#   * coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
# Example 2:
#   * coins = [2], amount = 3
# return -1.
#
# Note: You may assume that you have an infinite number of each kind of coin.

def coin_change(coins, amount):
    counts = [amount+1 for i in xrange(amount + 1)]
    counts[0] = 0
    for a in xrange(1, amount + 1):
        for c in coins:
            if a >= c:
                counts[a] = min(counts[a], counts[a-c] + 1)
    return counts[amount] if counts[amount] < amount + 1 else -1

print coin_change([1,2,5], 11)

