class Solution(object): 
    def numberOfSpecialChars(self, word): 
        """ :type word: str :rtype: int """ 
        sma=[] 
        caps=[] 
        for x in word: 
            if x.islower(): 
                sma.append(x) 
            else: caps.append(x.lower()) 
        co=0 
        for x in set(sma): 
            if x in caps and word.rfind(x)< word.find(x.upper()): 
                caps.remove(x) 
                co+=1 
        return co