class Solution:
    def isValid(self, s: str) -> bool:
        myDic = {"(":")","[":"]","{":"}"}
        myStack = []
        for c in s:
            if c in myDic:
                myStack.append(c)
            else : 
                if len(myStack)==0:
                    return False
                lastInStack = myStack.pop()
                if myDic[lastInStack] != c:
                    return False
        return len(myStack)==0

