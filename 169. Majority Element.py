
# coding: utf-8

# In[27]:


#169. Majority Element
#https://leetcode.com/problems/majority-element/description/
import math as m
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        nums.sort()
        print(m.floor(n/2),nums[m.floor(n/2)],nums[0])
        if nums[m.floor(n/2)] == nums[m.floor(n/4)] or nums[m.floor(n/2)] == nums[m.floor(3*n/4)]:
            return nums[m.floor(n/2)]
        else:
            return None


# In[28]:



nums = [3,2,3]
x = Solution()
y = x.majorityElement(nums)
print(y)

