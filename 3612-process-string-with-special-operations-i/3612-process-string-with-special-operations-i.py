class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for x in s:

            if x.isalpha():

                stack.append(x)

            elif x == "*":

                if stack:
                    stack.pop()

            elif x == "#":

                stack = stack + stack

            elif x == "%":

                stack.reverse()

        return "".join(stack)