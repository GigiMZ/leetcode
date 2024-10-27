def containsDuplicate(nums: list[int]) -> bool:
    dc = {}
    for i in nums:
        if dc.get(i) is not None:
            dc[i] = dc[i] + 1
            if dc[i] == 2:
                return True
            else:
                dc[i] = 1
        ls = list(dc.values())
        if not ls.__contains__(2):
            return False


# tried

def maxProfit(prices: list[int]) -> int:
    while True:
        if prices.index(max(prices)) < prices.index(min(prices)) and prices.index(min(prices)) < len(prices)/2:
            prices.remove(max(prices))
        elif prices.index(max(prices)) < prices.index(min(prices)) and prices.index(min(prices)) > len(prices)/2:
            prices.remove(min(prices))
        else:
            return max(prices) - min(prices)


# chatgpt
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    last_seen = {}  # Dictionary to store the last seen index of each element

    for i, num in enumerate(nums):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i  # Update the last seen index of the current element

    return False


def missingNumber(nums: list[int]) -> int:
    nums.sort()
    for i in range(len(nums)+1):
        if i == len(nums):
            return i
        elif i != nums[i]:
            return i


def moveZeroes(nums: list[int]) -> None:
    count = 0
    i = 0
    while True:
        if i == len(nums):
            break
        if nums[i] == 0:
            count += 1
            nums.pop(i)
        else:
            i += 1
    for i in range(count):
        nums.append(0)


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    ls = set([])
    for num in nums1:
        if nums2.__contains__(num):
            ls.add(num)
    return list(ls)


# trying
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    ls = []
    if len(nums1) > len(nums2):
        numm = nums1
        nums1 = nums2
        nums2 = numm
    for num in nums1:
        if nums2.__contains__(num):
            ls.append(num)
    return ls


def isAnagram(s: str, t: str) -> bool:
    s = sorted(s)
    t = sorted(t)
    if s == t:
        return True
    return False
