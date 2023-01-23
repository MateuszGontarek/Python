pos = []
n = int(input())
correctAnswer = []

def check(pos, x, y):
    for i in range(len(pos)):
        x_diff = abs(i - x)
        y_diff = abs(pos[i] - y)
        if pos[i] == y or x_diff == y_diff:
            return False
    return True

def hetmans():
    for i in range(n):
        if len(pos) == n: 
            correctAnswer.append(pos[:])
            break
        if check(pos, len(pos), i):
            pos.append(i)
            hetmans()
            pos.pop()

hetmans()
print(len(correctAnswer))