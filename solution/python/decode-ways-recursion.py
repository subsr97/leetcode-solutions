"""
Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Constraints:
    1 <= s.length <= 100
    s contains only digits and may contain leading zero(s).

"""

class Solution:
    
    num_to_alpha_dict = {str(num): chr( ord("A") + num-1 ) for num in range(1,27)}    
    ways = 0
    
    # Dictionary for memoization
    ways_dict = dict()
    
    def decode_message(self, s):
        
        current_ways = self.ways

        if s == "":
            self.ways += 1
            return
        
        # Checking if subsctring is already memoized.
        if s in self.ways_dict:
            self.ways += self.ways_dict[s]
            return
        
        if s[0] in self.num_to_alpha_dict:
            self.decode_message(s[1:])
        
        if len(s) >= 2 and s[0:2] in self.num_to_alpha_dict:
            self.decode_message(s[2:])
        
        # If a valid solution has been found with this subsctring, number of ways would have increased.
        # Memoizing the number of ways for this substring.
        if self.ways > current_ways:
            self.ways_dict[s] = self.ways - current_ways
    
    def numDecodings(self, s: str) -> int:    
        
        self.decode_message(s)
        
        print(self.ways_dict)

        return self.ways