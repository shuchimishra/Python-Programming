
# coding: utf-8

# In[44]:


#171. Excel Sheet Column Number
#https://leetcode.com/problems/excel-sheet-column-number/description/
class Solution:
    def titleToNumber(self,s):
        """
        :type s: str
        :rtype: int
        """
        newstr = s[::-1]
        sum = 0
        for i,val in enumerate(newstr):
            sum = sum + ((ord(val) - 64) * (26 ** i))
        return sum


# In[42]:


import unittest
class TestMap ():
    def test_map_1 (self):
        s = 'AAR'
        sol = 720
        x = Solution()
        self.assertEqual(x.titleToNumber(s),sol)
a = TestMap()
# unittest.TextTestRunner().run(a)

suite = unittest.TestLoader().loadTestsFromModule(a)
unittest.TextTestRunner().run(suite)

