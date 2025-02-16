def permute(s, storing_all_combinations = ""):
    if len(s) == 0 :
        print( storing_all_combinations )

    else :

        for i in range(len(s)): 

            char  = s[i] 

            remaining = s[:i] + s[i+1:]

            permute(remaining, storing_all_combinations  + char)    

string = "abc"
print("All permutations of", string, "are:")
permute(string)

# collections .perumations

# from itertools import permutations

# def all_permutations(s):
#     perm_list = permutations(s)  
#     for perm in perm_list:
#         print("".join(perm))  


# string = "abc"
# print("All permutations of", string, "are:")
# all_permutations(string)
