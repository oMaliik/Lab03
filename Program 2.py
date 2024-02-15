numbers = []
print("Enter 10 values:")
for i in range(10):
    num = int(input(f"Enter Number {i+1} :"))
    numbers.append(num)

largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i

print(f"\nThe largest number is {largest}")