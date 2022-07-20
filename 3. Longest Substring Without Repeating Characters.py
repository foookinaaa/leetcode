# https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


# my des
def lengthOfLongestSubstring(s: str) -> int:
    # boundary case
    if len(s) == 0:
        return 0
    l = 0
    r = 1
    # if only one element
    max_cnt = 1
    cur = s[l]
    while r < len(s):
        # substring
        if s[r] not in cur:
            cur += s[r]
            r += 1
        else:
            max_cnt = max(max_cnt, len(cur))
            # cut cur
            cur = s[l:r]
            l += 1
        print(cur)
    max_cnt = max(max_cnt, len(cur))
    return max_cnt


# des opt
def lengthOfLongestSubstring1(s):
    start = maxLength = 0
    usedChar = {}

    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i
    return maxLength

# des opt
def lengthOfLongestSubstring2(s):
    """
    :type s: str
    :rtype: int abcabcbb
    """
    if len(s) == 0:
        return 0
    seen = {}
    left, right = 0, 0
    longest = 1
    while right < len(s):
        if s[right] in seen:
            left = max(left, seen[s[right]] + 1)
        longest = max(longest, right - left + 1)
        seen[s[right]] = right
        right += 1
        print(left, right, longest)
    return longest
