from sys import argv

script, from_file, to_file = argv

indate = open(from_file).read()
out_file = open(to_file, 'w').write(indate)

