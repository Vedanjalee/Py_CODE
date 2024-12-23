arr = [-5, 2, 9, -3, 0, 1]
nega =[]
posi =[]
for a in arr:
    if a >= 0:
        posi.append(a)
    else:
        nega.append(a)
print(posi+nega)            
        