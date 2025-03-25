# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution(object):
    def power(self,x,n):
        if n==0:
            return 1
        if n<0:
            return 1/self.power(x,-1*n)

        num=self.power(x,n//2)
        if n%2==0:
            return num*num
        return x*num*num

    def myPow(self, x, n):
        return self.power(x,n)

        
            





        # num=pow(x,n)
        # num2=float(num)
        # return num2
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        