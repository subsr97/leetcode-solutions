# Product of Array Except Self 

## Using two arrays

Calculate left and right arrays such that:
* left[i] holds the product of elements to the left of nums[i]
* right[i] holds the product of elements to the right of nums[i]
* left[i] = right[l-1] = 1

Calculate the ans using : `ans[i] = left[i-1] * ans[i+1]`

**Time Complexity:** O(n)

**Space Complexity:** O(n)


## Using a single array

Similar to previous approach, calculate left array. (Answer will be stored in this array)

For right, instead of having a separate array, use a variable.

Iterate through the array and update R and ans[i] in each iteration.

**Time Complexity:** O(n)

**Space Complexity:** O(1) (Excluding ans array)