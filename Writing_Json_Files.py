import json
#Creating JSON files

employee = {"full_name":"John Doe",
            "age":25,
            "job":"Software Engineer",}

file_path = "output.json"

try:
    with open(file_path,"w") as file:
        json.dump(employee, file, indent = 2)
        print(f"The JSON file {file_path} has been updated.")
except PermissionError:
    print("Error, you do not have permission to write to this location.")
except Exception as e:
    print(f"Something went wrong, technical details: {e}.")


