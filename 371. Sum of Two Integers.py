
# coding: utf-8

# In[31]:


#371. Sum of Two Integers
#https://leetcode.com/problems/sum-of-two-integers/description/
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        l = [0,0]
        l[0] = a
        l[1] = b
        return sum(l)


# In[32]:


import unittest
class TestMap ():
    def test_map_1 (self):
        a = 1
        b = 2
        sol = 3
        x = Solution()
        self.assertEqual(x.getSum(a,b),sol)
a = TestMap()
# unittest.TextTestRunner().run(a)

suite = unittest.TestLoader().loadTestsFromModule(a)
unittest.TextTestRunner().run(suite)

