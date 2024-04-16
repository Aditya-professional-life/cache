class Solution:
    def dectoBinary(self,x):
        binary_string = ""
        for i in range(31, -1, -1):
            k = n >> i
            if (k & 1):
                binary_string += "1"
            else:
                binary_string += "0"
        return binary_string
    def convert_to_decimal(self,x):
        dec = 1
        for i in range(len(n)-1):
            dec = dec*2 + int(n[i+1])
        return dec
    
    
    
    def reversedBits(self, x):
        bin_num = self.dectoBinary(x).reverse()
        return self.convert_to_decimal(dec)
