# Simple recursive program to find factorial
def facto(num):
    if num == 1:
        return 1
    else:
        print(facto(num - 1))
        return num * facto(num - 1)


print(facto(3))
