class Solution(object):
    def missingNumber(self, nums):
        #sum of the array specified
        summ = sum(nums)
        #sum of the number from 0 to len(nums)
        newsum=0
        #make +1 for the length of the array so it can loop on the last element (index starting from 0)
        #get the sum of actual numbers that should been with the missing number
        for i in range(len(nums)+1):
            newsum+=i
        #if you got the actual sum and the sum you got by using substraction you will return the missing number
        return newsum-summ
        
        """
        :type nums: List[int]
        :rtype: int
        """
        