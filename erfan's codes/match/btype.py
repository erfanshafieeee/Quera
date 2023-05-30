stack = list()

string = input()

for ch in string:
    if ch != "=":
            stack.append(ch)
    else:
        if len(stack) > 0:
            stack.pop()

result = ""
for i in range(len(stack)):
    result += stack[i]

print(result)    