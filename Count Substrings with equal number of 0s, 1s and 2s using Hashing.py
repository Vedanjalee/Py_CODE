from collections import defaultdict 

def countSubstrings(s):
    freq_map = defaultdict(int) 
    freq_map [(0,0)] = 1

    count_0 = count_1 = count_2 = 0
    result = 0

    for ch in s :
        if ch == '0' :
            count_0 += 1
        elif ch == '1' :
            count_1 += 1
        elif ch == '2' :
            count_2 += 1


        diff0_1 = count_0 - count_1
        diff0_2 = count_0 - count_2

        result += freq_map[(diff0_1, diff0_2)]     

        freq_map[(diff0_1, diff0_2)] += 1
    return result

s = "0102010"
print(countSubstrings(s))           