#Operators- are symbol used to perform action on variables and values.
#Types- 
'''     Arithmetic 
        Comparision
        Logical
        Assignment
        Bitwise
        Membership
        Identity
'''

#1.Arithmetic- Used for mathematical calculations.

print(10 + 5) #Addition	
print(10 - 5) #Subtraction
print(10 * 5) #Multiplication
print(10 / 5) #Division
print(10 % 3) #Modulus(Remainder)
print(10 ** 2) #Power
print(10 // 3) #Floor Division

#2.Comparison- Used to compare two values. The answer is either True or False.

print(10 == 10)   #equal
print(10 != 5)    #not equal
print(10 > 5)     #greater than
print(10 < 5)     #less than
print(10 >= 10)   #greater or equal
print(10 <= 5)    #less pr equal

#3.Logical- Used with conditions.

#and- Returns True if both conditions are true.
print(10 > 5 and 8 > 3)

#or- Returns True if at least one condition is true.
print(10 > 5 or 2 > 8)

#not- Reverses the result.
print(not (10 > 5))

#4.Assignment- Used to assign values to variables.

x = 10
print(x)

x += 5
print(x)      #x = x+5

x -= 3
print(x)      #x= x-3

x *= 2
print(x)      #x = x*2

x /= 4
print(x)      #x = x/4

#5.Membership- Used to check whether a value is present in a list, string, or tuple.

#in- present 
fruits = ["apple", "banana", "mango"]
print("apple" in fruits)

#not in- not present
fruits = ["apple", "banana", "mango"]
print("grapes" not in fruits)

#6.Identity- Used to check whether two variables refer to the same object.

#is- same object(True)
x = [1, 2]
y = x
print(x is y)

#is not- diff object(False)
x = [1, 2]
y = [1, 2]
print(x is not y)

#7.Bitwise- Used to work with binary (0 and 1) values.

#and(&)- both bit true then 1(true)
print(5 & 3)

#or(|)- atleast one true then 1(true)
print(5 | 3) 

#XOR(^)- o/p 1 if both are different
print(5 ^ 3)

#NOT(~)- reverse
print(~5)

#Left Shift(<<)- moves bits to left
print(5 << 1)

#Right Shift(>>)- moves bits to right
print(5 >> 1)

