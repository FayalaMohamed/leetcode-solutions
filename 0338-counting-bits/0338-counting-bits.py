class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]*(n+1)
        highestPowerOfTwo = 1

        for i in range(1, n+1):
            if 2*highestPowerOfTwo == i:
                highestPowerOfTwo = i
            arr[i] = 1 + arr[i-highestPowerOfTwo]

        return arr