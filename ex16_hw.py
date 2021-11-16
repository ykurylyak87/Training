from sys import argv

script, file_name = argv

#Append to the end of the file
file = open(file_name, 'a')


line = input("Input line: ")
file.write(line + "\n")
file.close()

file = open(file_name)
print(file.read())

file.close()