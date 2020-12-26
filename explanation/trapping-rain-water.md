# Trapping Rain Water

## Bruteforce

Iterate over the array and for each element, find the amount of water that can be stored.

Which is -> minimum ( maximum height on left, maximum height on right) - current height.

**Time Complexity:** O(n^2)

**Space Complexity:** O(1)


## Dynamic Programming

Approach is similar to bruteforce.

But instead of finding left_max and right_max for every element, we pre-compute the values.

**Time Complexity:** O(n)

**Space Complexity:** O(n)


## Two Pointer Approach

If there is a larger bar at one end (say right), we are assured that the water trapped would be dependant on height of bar in current direction (from left to right). 

As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left). 

We must maintain left_max and right_max during the iteration, but now we can do it in one iteration using 2 pointers, switching between the two.

### Algorithm

* Initialize left pointer to 0 and right pointer to size-1
* While left < right, do:
  * If height[left] is smaller than height[right]
    * If height[left]≥left_max, update left_max
    * Else add left_max−height[left] to ans
    * Add 1 to left.
  * Else
    * If height[right]≥right_max, update right_max
    * Else add right_max−height[right] to ans
    * Subtract 1 from right.

**Time Complexity:** O(n)

**Space Complexity:** O(1)