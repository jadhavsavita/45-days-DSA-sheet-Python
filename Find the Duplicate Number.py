'''Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2'''

 def findDuplicate(self,nums):
    tot = nums[0]  
    har= nums[0]      
    while True:
        tot= nums[tot] 
        har = nums[nums[har]]    
        if tot == har:
            break
    
    tot = nums[0]  
    while tot != har:
        tot = nums[tot]
        har = nums[har]

    return tot
