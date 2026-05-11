class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        count=0
        j=0
        i=0
        res=""
        for i in range(len(s)):
            if s[i]=='(':
                count=count+1
            elif s[i]==')':
                count=count-1
            
            if count==0:
                res+=s[j+1:i]
                j=i+1
        return res