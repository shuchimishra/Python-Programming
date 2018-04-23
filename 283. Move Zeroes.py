
# coding: utf-8

# In[15]:


#283. Move Zeroes
#https://leetcode.com/problems/move-zeroes/description/
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        i = 0
        print(count)
        while i <= len(nums)-1:
            if nums[i] == 0:
                nums.pop(i)
            else:
                i = i + 1
        new_list = [0] * count
        nums.extend(new_list)
        return nums


# In[23]:


import unittest
from datetime import datetime
class TestMap ():
    def test_map_1 (self):
        nums = [0,0,1] 
        sol = [1,0,0]
        x = Solution()
        y = x.moveZeroes(nums)
        print(y)
        self.assertEqual(y,sol)
a = TestMap()
# unittest.TextTestRunner().run(a)

suite = unittest.TestLoader().loadTestsFromModule(a)
unittest.TextTestRunner().run(suite)

