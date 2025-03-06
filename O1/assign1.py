def smth(n):
    i = 0
    for ii in n:
        i += 1
    if n.isdigit() and i == 1:
        n = int(n) + int(n+n) + int(n+n+n) + int(n+n+n+n)
        return n
    else :
        return "Invalid"
value = input()
output = smth(value)
print(output)