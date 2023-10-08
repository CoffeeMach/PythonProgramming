# This program prints the numbers from 1 to 100
# Multiples of three are printed as "Fizz"
# Multiples of five are printed “Buzz”
# Multiples of both three and five are printed as “FizzBuzz”

number = 1

for number in range(1, 101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
print("Thank you for joining!")
