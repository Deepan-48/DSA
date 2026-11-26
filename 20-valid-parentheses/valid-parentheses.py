class Solution(object):
    def isValid(self, s):
        """
        stack=[]
        bracketMap={')':'(','}':'{',']':'[','>':'<'}
        for ch in s:
            if ch in bracketMap:
                if stack and stack[-1]==bracketMap[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return not stack
        












        """
        stack=[]
        bm={')':'(','}':'{',']':'['}
        for ch in s:
            if ch in bm:
                if stack and stack[-1]==bm[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return len(stack)==0