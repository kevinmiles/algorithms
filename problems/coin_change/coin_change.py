# coin_change.py

# You are given coins of different denominations and a total amount of money.
# Write a function to compute the fewest number of coins that you need to make
# that amount. If that amount cannot be made by any combination of the coins,
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


class Solution(object):

    def coin_change(self, coins, amount):
        d = [amount+1 for i in range(amount + 1)]
        d[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a >= c:
                    d[a] = min(d[a], d[a-c] + 1)
        return d[amount] if d[amount] < amount + 1 else -1

    def main(self):
        n = int(input())
        coins = list(map(int, input().split()))
        amount = int(input())
        result = self.coin_change(coins, amount)
        print(result)

if __name__ == "__main__":
    Solution().main()
