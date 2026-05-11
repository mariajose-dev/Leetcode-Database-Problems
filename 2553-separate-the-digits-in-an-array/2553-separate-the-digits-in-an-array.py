class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st=[]
        for x in nums:
            temp=[]
            while x!=0:
                r=x%10
                x=x//10
                temp.append(r)

            temp.reverse()   # correct order
            st.extend(temp)
        return st