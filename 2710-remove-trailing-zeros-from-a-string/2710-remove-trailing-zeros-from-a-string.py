class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        co=0
        for x in num[::-1]:
            co+=1
            if x!='0':
                break
        pos=len(num)-co+1
        return num[:pos]