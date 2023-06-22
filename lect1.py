#!/usr/bin/env python
# coding: utf-8

# In[1]:


class pair:
	def __init__(self):
		self.min = 0
		self.max = 0
 
def getMinMax(arr: list, n: int) -> pair:
	minmax = pair()
 
	# If there is only one element then return it as min and max both
	if n == 1:
		minmax.max = arr[0]
		minmax.min = arr[0]
		return minmax
 
	# If there are more than one elements, then initialize min
	# and max
	if arr[0] > arr[1]:
		minmax.max = arr[0]
		minmax.min = arr[1]
	else:
		minmax.max = arr[1]
		minmax.min = arr[0]
 
	for i in range(2, n):
		if arr[i] > minmax.max:
			minmax.max = arr[i]
		elif arr[i] < minmax.min:
			minmax.min = arr[i]
 
	return minmax
 
# Driver Code
if __name__ == "__main__":
	arr = [1000, 11, 445, 1, 330, 3000]
	arr_size = 6
	minmax = getMinMax(arr, arr_size)
	print("Minimum element is", minmax.min)
	print("Maximum element is", minmax.max)


# In[1]:


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
 
        return max_profit


# In[1]:


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
 
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
 
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
 
            max_so_far = temp_max
 
            result = max(max_so_far, result)
 
        return result


# In[1]:


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res
 
    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1



# In[2]:


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]


# In[ ]:




