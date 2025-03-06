def smth(n):
    n = (n.strip('[').strip(']').split(','))
    if any(x.isalpha() for x in n) or len(n)<3:
        return "Invalid"
    else:
        n = [int(x) for x in n]
        n.sort()
        left = n[0]*n[1]
        right = n[-1]*n[-2]
        if left > right and left != 0:
            return left
        elif right > left and right != 0:
            return right
        else:
            return "Invalid"
yolo = input()
out = smth(yolo)
print(out)