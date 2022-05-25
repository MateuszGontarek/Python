a = float(input("value ax^2: "))
b = float(input("value bx: "))
c = float(input("value c: "))
delta = pow(b,2) - 4*a*c
if delta > 0:
    x1 = (-b + pow(delta, 0.5))/2*a
    x2 = (-b - pow(delta, 0.5))/2*a
    print("x1: " + str(x1))
    print("x2: " + str(x2))
elif delta == 0:
    x = -b/(2*a)
    print("x: " + str(x))
else: print("no solutions")
