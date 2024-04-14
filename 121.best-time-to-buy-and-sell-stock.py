#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_sell_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            # min_sell_price = min(min_sell_price, price)
            # max_profit = max(max_profit, price - min_sell_price)
            if min_sell_price > price:
                min_sell_price = price
            if max_profit < price - min_sell_price:
                max_profit = price - min_sell_price

        return max_profit


# @lc code=end
# Time: O(n)
# Memory: O(1)
# Note:
# Using min max took more time since there are many thing overhead of it (Eg: checking if input is iterator ...)
