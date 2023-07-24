n = int(input("Enter the number of numbers : "))

numbers = []

for i in range(1, n+1):
    numbers.append(int(input("Enter the number : ")))
    
result = 0

for i in numbers:
    result = result + i
    
print(f"The result is : {result/n}")