class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
        #where the bin indicates the binary

        #the int (a , 2) indicates that the given value and it's conversion base number as 2

        #this will convert the binary to inyteger

        # now the both integer added , and the bin converts the integer into binary value , and there will be '0b' which indicates it as a binary , so we print it after 2 index
        