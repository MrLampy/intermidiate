def smth(n):
    n = n.split()
    hour = int(n[0])
    min = int(n[1])
    hour2 = int(n[2])
    min2 = int(n[3])
    dmin = min2 - min
    dhour = hour2-hour
    num = 0
    dh1 = dhour
    dm1 = dmin
    dm1 = (dh1*60)+dm1
    if ('-' in n) or any(char.isalpha() for char in n) or (hour>hour2) or (hour == hour2 and min>min2) or hour2 >= 24 or hour<0 or hour2<0 or min<0 or min2<0 or min >= 60 or min2 >= 60:
        return "Invalid"
    else:
        if dm1 <= 15:
            return 0
        else:
            if dmin > 0:
                dhour += 1
                dmin = 0
            if dhour<=3:
                num += dhour*10
                dhour -= 3
            elif dhour <=6:
                dhour-=3
                num = 30
                num += dhour*20
            else:
                num = 200
                dhour = 0
            return num
vo = input()
out = smth(vo)
print(out)