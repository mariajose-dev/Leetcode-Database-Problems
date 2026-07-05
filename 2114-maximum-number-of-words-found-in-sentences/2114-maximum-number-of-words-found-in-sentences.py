class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        lis=[]
        for x in sentences:
            co=0
            for s in x.split():
                co+=1
            lis.append(co)
        return max(lis)