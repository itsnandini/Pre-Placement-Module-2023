class Solution:
    def addStrings(self, num1, num2):
        result = ""
        carry = 0

        def equalizeNumberOfCharacters(num1, num2):
            if len(num1) < len(num2):
                while len(num1) != len(num2):
                    num1 = "0" + num1
            else:
                while len(num2) != len(num1):
                    num2 = "0" + num2
            return [num1,num2]
        
        num1, num2 = equalizeNumberOfCharacters(num1, num2)
        
        num1Array = list(num1)
        num2Array = list(num2)
        
        while len(num1Array) != 0:
            add = int(num1Array.pop()) + int(num2Array.pop()) + int(carry)
            carry = add // 10
            result = str(add % 10) + result
        
        if carry != 0:
            result = str(carry) + result
        return result        
