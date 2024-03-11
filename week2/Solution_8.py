class Solution_8:
    def myAtoi(self, s: str) -> int:
        i = 0
        isPos = True
        ans = ""

        # empty string
        if len(s) == 0: return 0

        # remove spaces
        while (i < len(s) and s[i] == ' '):
            i += 1
        
        # if i has reached the end, return 0
        if i == len(s): return 0

        # handle signs
        if s[i] == '-': 
            isPos = False
            i += 1
        elif s[i] == '+': 
            isPos = True
            i += 1
        
        # if i has reached the end, return 0
        if i == len(s): return 0

        # now check if num. 
        if not s[i].isdigit(): return 0

        # If num, handle overflow
        while (i < len(s) and s[i].isdigit()):
            ans += s[i]
            i += 1
        
        # if no number, return 0
        if len(ans) == 0: return 0

        # check limits
        if isPos:
            if int(ans) > 2**31-1: return 2**31-1
            else: return int(ans)
        else: # not positive
            if int(ans) > 2**31: return -2**31
            else: return -int(ans)

        return 0