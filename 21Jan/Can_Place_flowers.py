# def can_make_flowers(n, flowerbed):
#     f = [0] + flowerbed + [0]

#     for i in range(1, len(f)-1):

#         if f[i-1] == 0 and f[i] == 0 and f[i+1] ==0:
#             f[i] = 1

#             n -= 1
#     return n<=0        

def can_make_flowers(n, flowerbed):
    for i in range(len(flowerbed)):

        if flowerbed[i] == 0 :

            if (i==0 or flowerbed[i-1] == 0 )  and (i == len(flowerbed) - 1  or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                
                n -= 1
                
                if n<=0 :
                    return True 
    return n<=0 
                                                    
 

flowerbed =[1,0,0,0,1]
n =1

# true

print(can_make_flowers(n, flowerbed))