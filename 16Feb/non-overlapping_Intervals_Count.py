def non_overlapping(intervals) :
    intervals.sort()
    n = len(intervals) 
    if n==0:
        return 0 
    
    
    removal_count = 0 


    for i in range(n):
        for j in range(i+1, n) :

            if intervals[i][1] > intervals[j][0] and intervals[i][0] < intervals[j][1] :
                removal_count += 1
                break
   
    return removal_count       

print(non_overlapping([[1,2],[2,3],[3,4],[1,3]])) 
print(non_overlapping([[1,2],[1,2],[1,2]]))        
