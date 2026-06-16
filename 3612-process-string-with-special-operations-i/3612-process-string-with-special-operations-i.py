class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for x in s:
            if x>='a' and x<='z':
                stack.append(x)
            elif x == "*" and stack:
                stack.pop()
            elif x == "#" and stack:
                stack += stack
            elif x == "%" and stack:
                stack.reverse()

        return "".join(stack)