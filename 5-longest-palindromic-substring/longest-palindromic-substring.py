class Solution:
    def longestPalindrome(self, str: str) -> str:
        max_pal=""
        for center in range(len(str)):
            left=center
            right=center
            pal=""
            while left>=0 and right<len(str) and str[left]==str[right]:
                pal=str[left:right+1]

                if len(pal)>len(max_pal):
                    max_pal=pal
                left-=1
                right+=1
            left=center
            right=center+1
            pal=""
            while left>=0 and right<len(str) and str[left]==str[right]:
                pal=str[left:right+1]

                if len(pal)>len(max_pal):
                    max_pal=pal
                left-=1
                right+=1
        return max_pal