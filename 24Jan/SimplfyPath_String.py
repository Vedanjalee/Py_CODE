def simplifyPath(path):

    parts = path.split("/")
    new_path = []

    for part in parts : 
        if part == ".." : 
            if new_path : 
                new_path.pop() 

        elif part  == "." or part == "":
            continue 

        else:
            new_path.append(part)

    return "/" + "/".join(new_path)
                
path = "/home/../usr//bin/./scripts/"
print(simplifyPath(path))