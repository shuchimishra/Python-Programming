
# coding: utf-8

# In[79]:


#217. Contains Duplicate
#https://leetcode.com/problems/contains-duplicate/discuss/60850/One-line-solution-in-python
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        l_dist = len(set(nums))
        print(l,l_dist)
        if l != l_dist and l > 1:
            return True
        else:
            return False


# In[80]:


nums = [3,3]
x = Solution()
y = x.containsDuplicate(nums)
print(y)

