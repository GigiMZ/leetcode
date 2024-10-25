# def containsDuplicate(nums: list[int]) -> bool:
#     dc = {}
#     for i in nums:
#         if dc.get(i) != None:
#             dc[i] = dc[i] + 1
#             if dc[i] == 2:
#                 return True
#             else:
#                 dc[i] = 1
#         ls = list(dc.values())
#         if not ls.__contains__(2):
#             return False


def maxProfit(prices: list[int]) -> int:
    while True:
        if prices.index(max(prices)) < prices.index(min(prices)) and prices.index(min(prices)) < len(prices)/2:
            prices.remove(max(prices))
        elif prices.index(max(prices)) < prices.index(min(prices)) and prices.index(min(prices)) > len(prices)/2:
            prices.remove(min(prices))
        else:
            return max(prices) - min(prices)


print(maxProfit([2,4,1]))