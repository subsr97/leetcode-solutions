# Two Sum

## Bruteforce

Iterate over the array and for each element x, find if there is a value that is equal to (target-x).

**Time Complexity:** O(n^2)

**Space Complexity:** O(1)


## One-pass Hash Table

Iterate over the array and for each element, check if the complement (target-x) is present in the hashtable.

If not, add an entry for the current element.

**Time Complexity:** O(n)

**Space Complexity:** O(n)