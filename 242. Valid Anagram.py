
# coding: utf-8

# In[50]:


#242. Valid Anagram
#https://leetcode.com/problems/valid-anagram/description/
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s= ''.join(sorted(s))
        t = ''.join(sorted(t))
        if s == t:
            return True
        else:
            return False


# In[ ]:


s = "anagram"
t = ""
x = Solution()
y = x.isAnagram(s,t)
print(y)

