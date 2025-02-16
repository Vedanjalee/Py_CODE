def count_consonant_vowels(s):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTUVWXYZ"

    vowel_count = 0
    consonants_count = 0 

    for char in s : 
        if char in vowels: 
            vowel_count += 1
        elif char in consonants:
            consonants_count += 1 
    return   vowel_count ,  consonants_count

s= "hello wooorld"
vowels, consonants = count_consonant_vowels(s)
print("vowels: ",vowels  , "consonant : ", consonants )


