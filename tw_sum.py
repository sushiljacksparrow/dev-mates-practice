class Solution:

    def binary_search(self, numbers, start, end, value):
        if end >= start:
            mid = start + int((end - start)/2)
            if numbers[mid] == value:
                return mid
            if numbers[mid] > value:
                return self.binary_search(numbers, start, mid -1, value)
            else:
                return self.binary_search(numbers, mid + 1, end, value)
        else:
            return -1


    def twoSum(self, numbers, target):
        l = len(numbers)
        res = None
        for i in range(l-1):
            res = self.binary_search(numbers, i+1, l-1, target - numbers[i])
            if (res != -1):
                return [i+1, res + 1]

if __name__ == '__main__':
    sol = Solution()
    input = [2,7,11,15]
    res = sol.twoSum(input, 9)
    print(res)
