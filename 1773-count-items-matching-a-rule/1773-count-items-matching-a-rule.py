class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        co = 0
        if ruleKey == "type":
            pos = 0
        elif ruleKey == "color":
            pos = 1
        else:
            pos = 2
        for row in items:
            if ruleValue == row[pos]:
                co += 1
        return co
