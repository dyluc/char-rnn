# small helper script to remove indentations from copied movie scripts

file_name = "./datasets/original_trilogy_scripts.txt"

with open(file_name, "r") as file:
    content = file.readlines()

processed_content = [line if line.strip() == '' else line.lstrip() for line in content]

with open(file_name, "w") as file:
    file.writelines(processed_content)

print("Done.")
