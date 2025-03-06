def timeRequiredToBuy(tickets, k):
    time = 0

    for i in range(len(tickets)):
        if i<= k:
            time += min(tickets[i], tickets[k])

        else:
            time += min(tickets[i] , tickets[k] - 1)

    return time  

tickets = [2, 3, 2]
k = 1
print(timeRequiredToBuy(tickets, k))          


