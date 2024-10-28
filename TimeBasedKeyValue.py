class TimeMap(object):

    def __init__(self):
         self.data = {}
        

    def set(self, key, value, timestamp):
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((value,timestamp))
       

    def get(self, key, timestamp):
        if key not in self.data:
            return ""

        values = self.data[key]
        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return values[right][0] if right >= 0 else ""
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)