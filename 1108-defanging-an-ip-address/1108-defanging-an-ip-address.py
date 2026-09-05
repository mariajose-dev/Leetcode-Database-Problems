class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ans=""
        for x in address:
            if x=='.':
                ans+='[.]'
            else:
                ans+=x
        return ans