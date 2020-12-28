# Number of Islands

## Recursion

Traverse the grid recursively and sink lands by marking them as "-".

If a set of recursive call returns, it means that there are no adjacent lands to be sunk.

So increment the number of islands and start once again at the next land.

**Time Complexity:** O(m*n)

**Space Complexity:** O(m*n) (Stack space for recursion)