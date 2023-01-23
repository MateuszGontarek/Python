def f(x):
    return 2*x**2 
r = 100000000
first_value = float(input())
second_value = float(input())
acc = (second_value - first_value) / r 
area = 0
i = 0
while i * acc + first_value <= second_value:
    area += f(i*acc + first_value)
    i += 1
print(area * acc)
