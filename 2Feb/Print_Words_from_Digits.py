def print_spell(n, words):
    
    if n == 0:
        return
   
    print_spell(n // 10, words)
    
    digit = n % 10
    
    print(words[digit], end=" ")


n = int(input("Enter the input here: "))


words = ["zero", "one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine"]

print("Answer is: ", end="")


if n == 0:
    print(words[0])
else:
    print_spell(n, words)

# print()  
