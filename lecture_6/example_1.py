file_path = "temp.csv"

try:
    with open(file_path) as file:
        file.read()
    print("Success")
except FileNotFoundError as e:
    print(e)
    print(f"Couldn't open the file: {file_path}")

print("Done")
