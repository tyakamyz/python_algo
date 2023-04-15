# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    n = len(nums)

    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target: 
                return True
        
    return False

def twoPointer(nums, target):
    nums.sort()
    n = len(nums)
    left, right = 0, n-1

    while left < right:
        if nums[left] + nums[right] == target: 
            return True
        elif nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        
    return False

# 2, 1, 5, 7
# 4, 1, 9, 7, 5, 3, 16
print(twoPointer([4, 1, 9, 7, 5, 3, 16], 14)) 