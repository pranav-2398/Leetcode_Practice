class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res
    
s = Solution()
print(s.reverseBits(11111111111111111111111111111101))


# b = 100
# print(bin(b))
# res = 0
# for i in range(8):
#     print("i = ", i)
#     bit = (b >> i) & 1
#     print("Bin rep of bit :" , end = ' ')
#     print(bin(bit))
#     x = bit << (8 - i)
#     print("Bin rep of x :" , end = ' ')
#     print(bin(x))
#     res = res | (bit << (8 - i))
#     print("Bin rep of res :" , end = ' ')
#     print(bin(res))