def find_largest_word(dict):
    largest_word = ""
    for word in dict:
        if len(word) > len(largest_word):
            largest_word = word
    return largest_word


dict = ["apple", "banana", "strawberry", "pineapple", "watermelon"]
print("Largest word:", find_largest_word(dict))
