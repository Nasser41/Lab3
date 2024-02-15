numbers = []

print("Enter 10 values:")
for i in range(10):
    value = float(input(f"Enter value {i+1}: "))
    numbers.append(value)
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("The largest number in the list is:", largest)