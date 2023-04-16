# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentCount = 0
        maxCount = 0
        dict = {}
        
        for num in nums:
            dict[num] = 0

        for n in nums:
            if n-1 not in dict:
                next = n+1
                while next in dict:
                    currentCount += 1
                    next += 1
                maxCount = max(maxCount, currentCount)
                currentCount = 0

        return maxCount+1

solution = Solution()

#print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(solution.longestConsecutive([100,4,200,1,3,2]))