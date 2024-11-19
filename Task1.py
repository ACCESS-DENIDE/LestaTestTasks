#import time


##########################################

#   !ALL COMMENT BLOCKS ARE USED TO CONFIRM THE THEORY!
# 
#       Explanation:
#           I used bitwise operator ">>" which extracts specified amount of bits
#           And considering the operating principle of binary all numbers with 0 at the begining
#           are even, and with 1 not.


#       Advantages:
#           * processing time- this operation only extract bit and check it

#       Disadvantages:
#           * Scaling difficulty- this method can be used only with pow 2 (x^2) values
#           * Obviousness- you need a little bet more brain processing powers, to understand, what's going on,
#           than just read "value mod 2"(which is widely used)

##########################################


# Brief- Check, is the value even.
#
# value-input int value
#
# return 1 if value even, 0 otherwise
#
def isEven(value):

      return value % 2 == 0


# Brief- Check, is the value even.
#
# value-input int value
#
# return 1 if value even, 0 otherwise
#
def isEvenHomebrew(value):

    return (not((value>>0)&1))




val=int(input())

#timer_original=0.0
#timer_homebrew=0.0

#timer_original=time.perf_counter()
#print(isEven(val))
#timer_original=time.perf_counter()-timer_original

#timer_homebrew=time.perf_counter()
print(isEvenHomebrew(val))
#timer_homebrew=time.perf_counter()-timer_homebrew

#print("Original time: "+ str(timer_original))
#print("Homebrew time: "+ str(timer_homebrew))
