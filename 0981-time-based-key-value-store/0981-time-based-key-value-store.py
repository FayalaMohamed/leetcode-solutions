class TimeMap(object):

    def __init__(self):
        self.myDict = dict()

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.myDict : 
            self.myDict[key] = []
        self.myDict[key].append([value, timestamp])


        
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        values = self.myDict.get(key, [])
        l, r = 0, len(values)-1
        res = ""
        while l<=r : 
            m = (l+r)//2
            if values[m][1]<=timestamp:
                res = values[m][0]
                l = m+1
            else : 
                r = m - 1
        return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)