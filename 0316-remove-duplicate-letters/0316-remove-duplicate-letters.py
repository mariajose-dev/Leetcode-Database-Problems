class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        lastoccurencedict = {}
        stack=[]
        visited=set()

        for i in range(len(s)):
            lastoccurencedict[s[i]]=i
        
        for i in range(len(s)):
            if s[i] not in visited:
                while (stack and stack[-1] > s[i] and 
                lastoccurencedict[stack[-1]]>i):
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
        return ''.join(stack)
        
        