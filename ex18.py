def print_two(*args):
  arg1, arg2 = args
  print(f"arg1: {arg1}, arg2: {arg2}")

print_two("Yuriy", "Kurylyak")

def print_two_again(arg1, arg2):
  print(f"arg1: {arg1}, arg2: {arg2}")

print_two_again("Yuriy2", "Kurylyak2")

def print_one(arg1):
  print(f"arg1: {arg1}")

print_one("Yuriy3")

def print_none():
  print("I got nothing.")

print_none()