pi = 3
a = 2

for i in range(1,16):
    if i%2 == 0:
       pi = pi - 4/(a*(a+1)*(a+2))
    else:
       pi = pi + 4/(a*(a+1)*(a+2))
    a += 2
print(pi)
  