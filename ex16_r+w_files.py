from sys import argv

script, file_name = argv

print(f"We're going to erase {file_name}.")
print("If you don't want that hit CTRL+C (^C).")
print("If you do want that hit RETURN.")

input("?")

print("Open the file ...")
#Write to the file, but first truncate
target = open(file_name, 'w')

print("Truncating the file .. Goodbye")
target.truncate()

print("Now I am going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these into the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And finally, we close it")
target.close()