def Compression_array_of_chars(chars):

    compressed =[]

    n = len(chars) 
    i = 0 

    while i < n :
        char = chars [i] 
        count = 1 

        while i+1 < n and chars[i] == char[i+1]:
            count += 1
            i += 1

        compressed.append(char)

        if count> 1 :
            compressed.extend(list(str(count)))
        

        i+=1
    chars [:len(compressed)] = compressed
    return len(compressed)


        

chars=['a', 'a', 'b', 'b', 'b', 'c', 'c', 'a']
new_length = Compression_array_of_chars(chars)
print("Compressed Array", chars[:new_length]) 
print("new length" , new_length)

            


            

        

        

   