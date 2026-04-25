import csv
#Creating CSV Files

employees = [["Name","Age","Martial_Art"],
             ["John",25,"Karate"],
             ["Charlie",27,"Muay Thai"],
             ["James",29,"Taekwondo"]]

file_path = "output.csv"
try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"The CSV file {file_path} was created.")
except PermissionError:
    print("You do not have permission to edit this file.")
except Exception as e:
    print(f"Error, something went wrong. Technical details: {e}.")


