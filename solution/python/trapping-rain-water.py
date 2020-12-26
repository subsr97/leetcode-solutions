"""
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
0 <= n <= 3 * 10^4
0 <= height[i] <= 10^5
"""

### DP Solution
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l = len(height)
        
        left_max_arr = [max(height[0:i]) if i != 0 else 0 for i in range(l)]
        right_max_arr = [max(height[i+1:l]) if i!= l-1 else 0 for i in range(l)]
        
        for i in range(l):
            
            if i == 0 or i == l-1:
                continue
            
            ## Brute Force
            # left_max = max(height[0:i])
            # right_max = max(height[i+1:l])
            
            left_max = left_max_arr[i]
            right_max = right_max_arr[i]
            
            tempAns = min(left_max, right_max) - height[i]
            
            if tempAns > 0:
                ans += tempAns
            
        
        return ans

## Two Pointer Solution
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        left_max = right_max = 0
        
        ans = 0
        
        while left < right:
            
            if height[left] < height[right]:
                
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                
                left += 1
            
            else:
                
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                    
                right -= 1
        
        return ans
                