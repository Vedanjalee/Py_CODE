def Anagram(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()

    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ","")

    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)

    return s1_sorted == s2_sorted  

print(Anagram("Listen", "Silent"))  
print(Anagram("Hello", "Olelh"))    
print(Anagram("Test", "Taste"))
