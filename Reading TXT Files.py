#Reading TXT Files

file_path = "C:/Users/44735/Desktop/output.txt"
with open(file_path, "r") as file:
    contents = file.read()
    print(contents)
    