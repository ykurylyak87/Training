from sys import argv

script, file_name = argv
#open file
txt = open(file_name)

print(f"Here's your file {file_name}:")
#read file
print(txt.read())
txt.close()

print("Type the file again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()