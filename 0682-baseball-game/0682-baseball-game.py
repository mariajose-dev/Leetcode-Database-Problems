class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        rec=[]
        for x in operations:
            if x not in ['C', 'D', '+']:
                rec.append(int(x))
            elif x=='C':
                rec.pop()
            elif x=='D':
                prod=2*rec[-1]
                rec.append(prod)
            elif x=='+':
                add=rec[-1]+rec[-2]
                rec.append(add)

        return sum(rec)