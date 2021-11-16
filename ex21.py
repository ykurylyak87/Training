def add(a, b):
  print(f"ADDING {a} + {b}")
  return a + b

def subrtact(a, b):
  print(f"SUBTRACTING {a} - {b}")
  return a - b

def multiply(a, b):
  print(f"MULTIPLYING {a} * {b}")
  return a * b

def divade(a, b):
  print(f"DIVIDING {a} / {b}")
  return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subrtact(84, 10)
weight = multiply(40, 2)
iq = divade(150, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle")

what = add(age, subrtact(height, multiply(weight, divade(iq,2))))

print("That becomes:", what, "Can you do it by hands?")

test = add(int(input("first number: ")), int(input("second number: ")))
print(f"Test = {test}")


def return_test(a):
  print("I remember what you input")
  return a

c = return_test(input("Please input your test: "))
print(c)
