
import math 

y = float(input("What would you like you value of y to be? "))

x = [10,20,30,40,50]
output_hy = []
print(x)

for point in x:
    output = math.hypot(point, y)
    output_hy.append(output)

print(output_hy)