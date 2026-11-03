import math

def relative_error(approx, exact):
    return abs(approx - exact) / abs(exact)

print(relative_error(3.14, math.pi))
print(relative_error((0.1 + 0.2), 0.3))

s = 0
for i in range(1000000):
    s += 0.1
print(relative_error(s, math.fsum([0.1] * 1000000)))