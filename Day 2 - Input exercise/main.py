#program that adds the digits in a 2 digit number
print("Enter a two digit number:")
number = int(input())
#Get the digits using modulus
first_digit = number % 10
second_digit = number // 10
#Add the digits together
result = first_digit + second_digit
#Print the result
print("The sum of the digits is " + str(result))





