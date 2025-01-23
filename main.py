with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("students.txt", "r") as file:
    for line in file:
        print(line[1])
        
with open("students.txt", "r") as file:
    for line in file:
        if len(line) > 6:
            print (line.strip())
        
with open ("students.txt" , "r") as file:
    for line in file :
        new_line = input ("enter a name:")
        with open ("students.txt" , "a") as file:
            file.write(new_line + "\n")
        