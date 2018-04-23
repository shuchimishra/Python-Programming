
# coding: utf-8

# In[53]:


#136. Single Number
#https://leetcode.com/problems/single-number/description/
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """           
        sing_num = [i for i in nums if nums.count(i) == 1]
        return sing_num[0]


# In[54]:


import unittest
from datetime import datetime
class TestMap (TestCase):
    def test_map_1 (self):
        nums = [2,2,1]
        sol = 1
        start_time = datetime.now()
        x = Solution()
        self.assertEqual(x.singleNumber(nums),sol)
        end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
a = TestMap()
# unittest.TextTestRunner().run(a)

suite = unittest.TestLoader().loadTestsFromModule(a)
unittest.TextTestRunner().run(suite)

