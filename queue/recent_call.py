class RecentCounter:
    request_list = []
    def __init__(self):
        self.request_list = []
        pass
        

    def ping(self, t: int) -> int:
        self.request_list.append(t)
        min_val = t - 3000
        max_val = t
        print(min_val,max_val)

        while self.request_list[0] < min_val:
            self.request_list.pop(0)
        print(self.request_list)
        return len(self.request_list)
    
[[],[642],[1849],[4921],[5936],[5957]]

obj = RecentCounter()
print(obj.ping(642))
print(obj.ping(1849))
print(obj.ping(4921))
print(obj.ping(5936))
print(obj.ping(5957))
