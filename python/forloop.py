"take inputs from the user until she preses b(disk to press b to quit after every integer input)print average and product of the numbers"
numbers = []
while True:
    user_input = input("Enter an integer (type b to quit): ")
    if user_input == 'b':
        break
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid integer or 'b' to quit.")

if numbers:
    average = sum(numbers) / len(numbers)
    product = 1
    for num in numbers:
        product *= num
    print("Average:", average)
    print("Product:", product)
else:
    print("No numbers were entered.")