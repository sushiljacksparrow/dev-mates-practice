
class Solution:
    def possiblePalindrome(self, left: int, right: int, s: str) -> bool:
        flag = True
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                flag = False
                break
            left = left - 1
            right = right + 1
        if flag:
            return True
        return False

    def shortestPalindrome(self, s: str) -> str:
        mid = int(len(s)/2)
        res = 0
        for i in range(mid, -1, -1):
            # check for both odd and even length cases mid and left of mid
            if self.possiblePalindrome(i - 1, i + 1, s):
                res = i
                break
            if self.possiblePalindrome(i - 1, i, s):
                res = i
                break

        print(res)
        temp = t[2*res+1:]
        rev = ''
        for i in range(len(temp)):
            rev = rev + temp[len(temp)-i-1]
        res = rev + t
        return res


if __name__ == '__main__':
    s = Solution()
    t = 'ba'
    res = s.shortestPalindrome(t)
    print(res)
