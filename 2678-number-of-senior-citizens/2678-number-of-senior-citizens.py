class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        co=0
        for x in details:
            ag=int(x[-4:-2])
            if ag>60:
                co+=1
        return co