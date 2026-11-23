class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str=s.lower()
        str=re.sub(r'[^a-zA-Z0-9\s]','',str)
        str=str.replace(" ","")
        left=0
        right=len(str)-1
        while left<right:
            if str[left]!=str[right]:
                return False
            left+=1
            right-=1
        return True
        