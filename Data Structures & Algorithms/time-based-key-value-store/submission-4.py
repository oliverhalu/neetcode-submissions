class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map.setdefault(key, []).append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map.get(key)
        if not values: return ""
        left, right = 0, len(values) - 1
        max_timestamp = -1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                max_timestamp = values[mid][1]
                left = mid + 1
            else: 
                right = mid - 1
        
        if max_timestamp != -1: 
            for v,t in values:
                if t == max_timestamp:
                    return v
        else:
            return ""



