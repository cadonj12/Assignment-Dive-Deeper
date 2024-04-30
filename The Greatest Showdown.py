#Task 1

number_one = float(input("First number: "))
number_two = float(input("Second number: "))
number_three = float(input("Third number: "))

largest_number = number_one

if number_two > largest_number:
    largest_number = number_two

if number_three > largest_number:
    largest_number = number_three

print("The largest number is:" , largest_number)