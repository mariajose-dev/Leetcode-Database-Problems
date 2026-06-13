class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        s="abcdefghijklmnopqrstuvwxyz"
        lis=[]
        for w in words:
            sum=0
            for x in w:
                if x in s:
                    pos=s.find(x)
                    sum+=weights[pos]
            lis.append(sum)

        ans=""
        rev = "zyxwvutsrqponmlkjihgfedcba"

        for x in lis:

            ans += rev[x % 26]

        return ans
        
