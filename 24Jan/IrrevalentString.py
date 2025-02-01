def isIrrelevantString(s, valid_chars):
    for char in s:
        if char not in valid_chars:
            return True  
    return False  


valid_set = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

string1 = "Hello123"
string2 = "Hello@123"


print("Is string1 irrelevant? :", isIrrelevantString(string1, valid_set)) 
print("Is string1 irrelevant? :", isIrrelevantString(string2, valid_set)) 
