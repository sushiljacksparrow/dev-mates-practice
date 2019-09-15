class Solution:
    def reverseWords(self, s: str) -> str:
        print(s)
        sentence_len = len(s)
        words = s.split(' ')
        print(words)

if __name__ == '__main__':
    sol = Solution()
    input: "the sky is blue"
    sol.reverseWords(input)
