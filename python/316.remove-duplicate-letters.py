#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Medium (39.97%)
# Likes:    7413
# Dislikes: 479
# Total Accepted:    250.7K
# Total Submissions: 542.6K
# Testcase Example:  '"bcabc"'
#
# Given a string s, remove duplicate letters so that every letter appears once
# and only once. You must make sure your result is the smallest in
# lexicographical order among all possible results.
# 
# 
# Example 1:
# 
# 
# Input: s = "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: s = "cbacdcbc"
# Output: "acdb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of lowercase English letters.
# 
# 
# 
# Note: This question is the same as 1081:
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# 
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        for letter in s:
            if len(stack) == 0:
                stack.append(letter)
            else:
                if letter in stack:
                    counter[letter] -= 1
                    continue

                while len(stack) > 0 and stack[-1] > letter:

                    if counter[stack[-1]] <= 1:
                        break
                    counter[stack[-1]] -= 1
                    stack.pop()

                stack.append(letter)

        return "".join(stack)
# @lc code=end

