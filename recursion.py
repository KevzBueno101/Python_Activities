def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25))

#step by step explanation 
#fun(25) = 25 + fun(28)
#fun(28) = 28 + fun(31)
#fun(31) = 3   (since 31 > 30)

#fun(28) = 28 + 3 = 31
#fun(25) = 25 + 31 = 56
