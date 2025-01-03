n = int(input())
x = 0
for i in range(n):
    operation = input().lower().strip()
    if operation == "++x" or operation == "x++":
        x += 1
    elif operation == "--x" or operation == "x--":
        x -= 1
print(x)
