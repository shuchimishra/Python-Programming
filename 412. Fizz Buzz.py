
# coding: utf-8

# In[68]:


#412. Fizz Buzz
#https://leetcode.com/problems/fizz-buzz/description/
class Solution:
    def mapper(self,y):
        if (y+1) % 3 == 0:
            if (y+1) % 5 == 0:
                return "FizzBuzz"
            else:
                return "Fizz"
        elif (y+1) % 5 == 0:
            return "Buzz"
        else:
            return str(y+1)
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        x = list(range(n))
        num = map(self.mapper,x)
        return list(num)


# In[69]:


from unittest import *
class TestMap (TestCase):
    def test_map_1 (self):
        n = 15
        sol = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        x = Solution()
        self.assertEqual(x.fizzBuzz(n),sol)
a = TestMap()
# unittest.TextTestRunner().run(a)

suite = unittest.TestLoader().loadTestsFromModule(a)
unittest.TextTestRunner().run(suite)

