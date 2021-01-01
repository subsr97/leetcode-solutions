"""
Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or 
suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of space complexity analysis.)

"""

# Using two arrays
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l = len(nums)
        
        left = [nums[0]]
        
        
        for num in nums[1:]:
            left.append( num*left[-1] )
            
        
        right = [nums[-1]]
        
        for num in nums[-2::-1]:
            right.insert(0, num*right[0] )
        
        
        ans = []
        
        for i in range(l):
            current_ans = 1
            
            if i-1 >= 0:
                current_ans *= left[i-1]
            
            if i+1 < l:
                current_ans *= right[i+1]
            
            ans.append(current_ans)
        
        return ans
            
            
        
# Using a single array
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array 
        length = len(nums)
        
        # The answer array to be returned
        answer = [0]*length
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1;
        for i in reversed(range(length)):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer