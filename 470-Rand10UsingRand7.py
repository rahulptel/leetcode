# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # i0 = rand7() % 7
        # i1 = rand7()
        agg = ((rand7() - 1) * 7) + rand7()
        while agg < 1 or agg > 10:
            agg = ((rand7() - 1) * 7) + rand7()
                    
        return agg
