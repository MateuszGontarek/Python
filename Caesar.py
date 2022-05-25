def funkcja(text,p):
    textReturn = ""
    for i in text:
        if i.islower():
            i = ((ord(i) + p - 97) % 26 + 97)
        elif i.isupper():
            i = ((ord(i) + p - 65) % 26 + 65)
        elif i.isdigit():
            i = (ord(i) + p - 48) % 10 + 48
        textReturn += chr(i)
    return textReturn


text = input()
p = int(input())

chec = int(input("Co chesz zrobić: "))
print("1. Szyfracje")
print("2. Deszyfracje")
print(text)
if chec == 2:
    p *= -1
    print(funkcja(text,p))
else:
    print(funkcja(text,p))