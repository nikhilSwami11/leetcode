class Solution:
    def magicalString(self, n: int) -> int:
        arr = ['1','2','2']
        one_count = 1

        if n <=3:
            return one_count
        
        last = 2
        while len(arr) <= n:

            group_length = int(arr[last])
            
            next_char = '1' if arr[-1] == '2' else '2'

            if next_char == '1':
                one_count += min(group_length, n - len(arr))
            
            arr.extend([next_char] * group_length)
            last+=1
        
        return one_count

print(Solution().magicalString(6))