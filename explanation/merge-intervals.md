# Merge Intervals

## Solution

Sort the list. 

Iterate the list and consider two intervals at a time.

If the ranges overlap, merge them into one, pop both of them and insert the new one.

If the ranges do not overlap, go to the next pair.

**Time Complexity:** O(nlogn) (Sorting)

**Space Complexity:** O(1)