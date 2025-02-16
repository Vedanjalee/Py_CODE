def generate_subsets(s, index =0 , current = ""):
    if index == len(s) : 
        print(current) 
        return

    generate_subsets(s, index+1, current + s[index])

    generate_subsets(s, index+1, current) 

string = "abc"
print("All subsets of", string, "are:")
generate_subsets(string)    



