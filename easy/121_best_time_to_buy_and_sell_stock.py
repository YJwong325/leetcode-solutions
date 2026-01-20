# Author: Yuan Jie Wong
# Last Updated: 2025-05-20

def maxProfit(self, prices):
    l = 0
    r = 1
    profit = 0

    while r < len(prices):
        if prices[r] < prices[l]:
            l = r
        else:
            profit = max(prices[r] - prices[l], profit)
        r += 1

    return profit