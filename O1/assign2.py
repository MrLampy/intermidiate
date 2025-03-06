def smth(n):
    def palindome(n):
        love = len(n)
        i = 0 
        check = 0
        while love > i:
            if n[love-1] != n[i]:
                check = 1
                break
            love = love-1
            i = i+1
        if check == 0:
            return 1
        else:
            return 0

    here = 0
    one = 0
    two = 0
    if n == '0' or n == '1' or not n.isdigit():
        return "Invalid"
    else:
        for ii in range(int(int(n)*'9'),-1,-1):
            for iii in range(int(int(n)*'9'),-1,-1):
                if palindome(str(ii*iii)) == 1:
                    if ii + iii > one + two:
                        one = ii
                        two  = iii
        return one*two
vo = input()
output = smth(vo)
print(output)