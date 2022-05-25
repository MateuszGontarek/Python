n = int(input())
is_prime = [True] * (n + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(pow(n + 1, 0.5))):
    if is_prime[i] == True:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
    print(i)

for i in range(n):
    if is_prime[i]:
        print(i, end=" ")