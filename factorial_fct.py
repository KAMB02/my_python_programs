def facto(x):
    if x<2:
        return 1
    else:
        return x*facto(x-1)


print(facto(10))