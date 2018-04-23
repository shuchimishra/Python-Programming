
# coding: utf-8

# In[26]:


#Reverse String
#https://leetcode.com/problems/reverse-string/description/
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


# In[27]:


from unittest import *
class TestMap (TestCase):
    def test_map_1 (self):
        s = "hello"
        x = Solution()
        self.assertEqual(x.reverseString(s),"olleh")
a = TestMap()
# unittest.TextTestRunner().run(a)

suite = unittest.TestLoader().loadTestsFromModule(a)
unittest.TextTestRunner().run(suite)

