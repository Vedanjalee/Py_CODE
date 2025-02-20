def generate_unique_permutations(s, curr_permu = "", used = set()):
    if len(curr_permu) == len(s) :
        print(curr_permu)
        return 

    for i in range(len(s)):
        if i in used : 
            continue 

        used.add(i) 

        generate_unique_permutations(s, curr_permu + s[i] , used) 

        used.remove(i) 

string = "aab"
print("Unique permutations of", string, "are:")
generate_unique_permutations(string)   