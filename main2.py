# Symbols	Values
# I	        1
# IV  	    4
# V	        5
# IX	    9
# X	        10
# XL	    40
# L	        50
# XC	    90
# C	        100
# CD	    400
# D	        500
# CM	    900
# M	        1000

# Function to convert integer to Roman values
def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            print(sym[i], end="")
            div -= 1
        i -= 1
# Driver code
if __name__ == "__main__":
    number = 3549
    print("Roman value is:", end=" ")
    printRoman(number)


    
import math
def integerToRoman(A):
    romansDict = \
        {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            5000: "G",
            10000: "H"
        }
    div = 1
    while A >= div:
        div *= 10
    div /= 10
    res = ""
    while A:
        # main significant digit extracted
        # into lastNum
        lastNum = int(A / div)
        if lastNum <= 3:
            res += (romansDict[div] * lastNum)
        elif lastNum == 4:
            res += (romansDict[div] +
                    romansDict[div * 5])
        elif 5 <= lastNum <= 8:
            res += (romansDict[div * 5] +
                    (romansDict[div] * (lastNum - 5)))
        elif lastNum == 9:
            res += (romansDict[div] +
                    romansDict[div * 10])
        A = math.floor(A % div)
        div /= 10
    return res
# Driver code
print("\nRoman value for the integer is:"
      + str(integerToRoman(3549)))

#output
Roman value is: MMMDXLIX
Roman value for the integer is:MMMDXLIX

Process finished with exit code 0
