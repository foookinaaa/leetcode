# https://leetcode.com/problems/permutation-in-string/
'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''
# my decision
from collections import Counter
def checkInclusion(s1: str, s2: str) -> bool:
    # counter substring
    d = Counter()
    for word in s1:
        d[word] += 1
    #print(d)
    stop = len(s1)
    for j in range(len(s2)-stop+1):
        cnt = Counter()
        # count substring slicing on 1 step
        for word in s2[j:stop]:
            cnt[word] += 1
        #print(cnt)
        if d == cnt:
            return True
        stop += 1
    return False

# des opt
def checkInclusion2(s1: str, s2: str) -> bool:
    '''
    - instead of generating a fresh freq hashmap for every new substring
    - build the freq dict for the initial window and then slide the window_dict
        (add/remove chars) by adjusting their frequinces.
    removing one preceding character and adding a new succeeding character to the new window
    '''

    k = len(s1)
    from collections import Counter
    d1 = Counter(s1)
    # initial window
    window = s2[:k]
    d2 = Counter(window)
    # check the intial window
    if d1 == d2:
        return True

    for i in range(len(s2)-k):
        # SLIDE THE WINDOW
        # 1 - remove s2[i]
        if d2[s2[i]] == 1:
            del d2[s2[i]]
        elif d2[s2[i]] > 1:
            d2[s2[i]] -= 1

        # 2- add s2[i+k]
        if s2[i+k] in d2:
            d2[s2[i+k]] += 1
        else:
            d2[s2[i+k]] = 1

        # check after sliding
        if d1 == d2:
            return True

    return False


