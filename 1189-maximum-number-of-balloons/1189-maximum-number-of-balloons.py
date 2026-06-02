class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        dic={}
        for x in text:
            if x in "balloon":
                if x in dic:
                    dic[x]+=1
                else:
                    dic[x]=1
                    
        return min(
            dic.get('b', 0),
            dic.get('a', 0),
            dic.get('l', 0) // 2,
            dic.get('o', 0) // 2,
            dic.get('n', 0)
        )  
        
