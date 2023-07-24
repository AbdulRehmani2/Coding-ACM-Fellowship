import time

startTime = time.time()

number = 0

for i in range(1, 10000):
    number = number + i
    
endTime = time.time()

print(f"The total time is {endTime - startTime}")    