def love(n):
    if ("-" in n) or len(n) > 20 or len(n) == 1 or any(char.isalpha() for char in n):
        return "Invalid"
    else:
        n = n.split()
        n.sort()
        i = 1
        while 1:
            if n[0] == '0':
                k = n[i]
                n[i] = '0'
                n[0] = k
                i = i + 1
            else:
                break

        return (''.join(n))

ho = input()
out = love(ho)
print(out)