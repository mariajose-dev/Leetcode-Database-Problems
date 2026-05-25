class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        clean_text = re.sub(r'[^\w\s]', ' ', paragraph)
        lower_text = clean_text.lower()

        st = lower_text.split()

        dic = {}

        for x in st:

            if x in dic:
                dic[x] += 1

            else:
                dic[x] = 1

        for y in sorted(dic, key=dic.get, reverse=True):

            if y in banned:
                continue

            else:
                return y
        


        