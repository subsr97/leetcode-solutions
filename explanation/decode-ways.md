# Decode Ways

## Recursion

This is a top-down approach.

Consume the string letter by letter, and recursively call the consuming function.

If the string can be consumed successfully, increment the number of ways.

**Time Complexity:** O(2^n)

**Space Complexity:** O(n) (Stack space for recursion)


## Recursion with memoization

Same a recursive approach, but when a possible solution is found,

memoize the substring and the number of ways associated with it.

## DP

This is a bottom-up approach.

Initialize dp array and base cases.

```
s = "231"
index 0: extra base offset. dp[0] = 1
index 1: # of ways to parse "2" => dp[1] = 1
index 2: # of ways to parse "23" => "2" and "23", dp[2] = 2
index 3: # of ways to parse "231" => "2 3 1" and "23 1" => dp[3] = 2
```

Iterate over remaining indices and check if valid numbers can be formed.

Increment current dp value accordingly.

**Time Complexity:** O(n)

**Space Complexity:** O(n)