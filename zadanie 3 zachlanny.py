def f(value):
    count = 0 
    while value > 0:
        for i  in [5, 3, 1]:
            if value - i >= 0:
                count += 1
                value -= i
                break
    return count

value = int(input())

print(f(value))