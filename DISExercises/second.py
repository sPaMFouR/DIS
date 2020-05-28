a = 2
b = 3


def have_fun(x, y):
    x += 2
    y += 3

print(a, b)
have_fun(a, b)
print(a, b)

# Call By Value


def have_fun1(x, y):
    x += [2]
    y += [3]

c = [2]
d = [3]

print(c, d)
have_fun1(c, d)
print(c, d)

# Call By Reference
