Rupees = 49

ans =[]

coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

n = len(coins)

for i in range(n - 1, -1, -1):

    while Rupees >= coins[i]:
        Rupees  -= coins[i]
        ans.append(coins[i])

print("The minimum number of coins is", len(ans))
print("The coins are : ")
for i in range(len(ans)):
    print(ans[i], end=" ")        
