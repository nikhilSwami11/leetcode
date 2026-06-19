class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        mid = (1<<(n-1))

        if k == mid:
            return "1"
        if k < mid:
            return self.findKthBit(n - 1, k)
        else:
            mirror_k = 2*mid - k
            k_bit_inverse = self.findKthBit(n-1,mirror_k)
            return "1" if k_bit_inverse=="0" else "0"
 

n = 3
k = 1
print(Solution().findKthBit(n,k))