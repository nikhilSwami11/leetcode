class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        reverse_digits = list(reversed(digits))
        print(reverse_digits)

        carry = 1
        for i in range(len(reverse_digits)):
            sum = reverse_digits[i] + carry
            reverse_digits[i] = sum % 10
            carry = sum // 10

        if carry == 1:
            reverse_digits.append(1)
        reverse_digits.reverse()

        return reverse_digits
    
print(Solution().plusOne([9]))