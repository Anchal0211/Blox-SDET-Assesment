
def add(num1_str, num2_str):
    try:
        num1 = int(num1_str)
        num2 = int(num2_str)

        result = num1 + num2

        result_str = str(result)

        return result_str

    except ValueError:
        return "Error: Invalid input. Please provide valid integers as strings."


# Input from the user
num1_str = input("Enter the first integer as a string: ")
num2_str = input("Enter the second integer as a string: ")

sum_str = add(num1_str, num2_str)

print("Sum:", sum_str)

