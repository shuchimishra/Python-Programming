
# coding: utf-8

# In[203]:


#387. First Unique Character in a String
#https://leetcode.com/problems/first-unique-character-in-a-string/description/
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_l = set(s)
        x = [s.index(val) for val in s_l if s.count(val) == 1]
        #print(x)
        return min(x) if len(x) >= 1 else -1


# In[204]:


s = ""
x = Solution()
y = x.firstUniqChar(s)
print(y)

