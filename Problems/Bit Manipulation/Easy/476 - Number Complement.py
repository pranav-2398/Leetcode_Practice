## STRING SOLN ######################################################################
class Solution:
    def findComplement(self, num: int) -> int:
        # Convert the number to binary representation
        binary_str = bin(num)[2:]  # Remove the '0b' prefix

        # Invert the bits
        inverted_str = ''.join(['1' if bit == '0' else '0' for bit in binary_str])

        # Convert back to decimal
        complement = int(inverted_str, 2)

        return complement

## BIT MANIPULATION SOLN #############################################################
class Solution:
    def findComplement(self, num: int) -> int:
        mask = 0
        temp = num
        
        # Create the mask with all bits set to 1 for the length of num
        while temp != 0:
            mask = (mask << 1) | 1
            temp >>= 1
        
        # XOR num with mask to get the complement
        return num ^ mask

#######################################################################################