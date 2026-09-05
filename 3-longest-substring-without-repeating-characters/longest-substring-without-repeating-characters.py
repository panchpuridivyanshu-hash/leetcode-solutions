class Solution:
    def lengthOfLongestSubstring(self, str):
        char=set()
        left=0
        max_len=0

        for ch in range(len(str)):
            while str[ch] in char:
                char.remove(str[left])
                left+=1

            char.add(str[ch])
            max_len=max(max_len,ch-left+1)
        return max_len

        