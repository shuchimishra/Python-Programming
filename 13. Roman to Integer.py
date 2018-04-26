
# coding: utf-8

# In[14]:


#13. Roman to Integer
#https://leetcode.com/problems/roman-to-integer/description/
class Solution:
    def romanToInt(self, s):
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)):
            current,next = s[i],s[i+1:i+2]
            if next and roman[current] < roman[next]:
                res = res - roman[current]
            else:
                res = res + roman[current]
        return res

        


# In[15]:


s = "MCMXCIV"
x = Solution()
y = x.romanToInt(s)
print(y)

