class TimeMap:
    def __init__(self):
        self.hash_table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_table.setdefault(key, []).append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
            res = ""
            items = self.hash_table.get(key , [])
            l = 0
            r = len(items) - 1
            while l <= r:
                mid = (l+r)//2
                if timestamp == items[mid][0]:
                    return items[mid][1]
                elif timestamp > items[mid][0]:
                    res = items[mid][1]
                    l = mid + 1
                else:
                    r = mid - 1
            return res
#Memory: O(m) -> number of set commands
#Time: O(nlogn) get | O(1) set