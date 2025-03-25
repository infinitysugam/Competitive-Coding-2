# We solve this using Dynamic Programming as there are repeated sub problem
# Time complexity = O(m*n)
#Space Complexity = O(m*n)

class Solution:
    def knapsack(self, W, val, wt):
        capacity = W
        profit = val 
        weights = wt
        n = len(val)

        dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

        for i in range(0, n+1):

            for w in range(0, capacity+1):

                if i == 0 or w == 0:

                    dp[i][w] = 0

                elif w < weights[i-1]:

                    dp[i][w] = dp[i-1][w]

                else:

                    dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]]+profit[i-1])

        return dp[n][capacity]