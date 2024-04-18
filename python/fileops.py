file_path = "sample.txt"

with open(file_path, "w") as file:
    file.writelines("this is python 10th experment\n")
    file.writelines("We are implemnting I/O in files.\n")

with open(file_path, "r") as file:
    content = file.readlines()
    print("Contents of the file:")
    print(content)

with open(file_path, "a") as file:
    file.writelines("Appending more text to the file.\n")

with open(file_path, "r") as file:
    updated_content = file.readlines()
    print("\nUpdated contents of the file:")
    print(updated_content)
file.close()