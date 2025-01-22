def min_num_platforms(arrival, departure ):

    arrival.sort()
    departure.sort() 

    i = 1 
    j = 0 

    platforms_needed = 1
    result = 1 

    while i<len(arrival) and j<len(departure):
        if arrival[i] <= departure[j] :
            platforms_needed += 1 
            i += 1
        
        else:
            platforms_needed -= 1  
            j += 1    

        result = max(result , platforms_needed)
    return result         

arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

print("Minimum platforms required:",min_num_platforms(arrival, departure ))