def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print(f"You have {cheese_count} cheeses!")
  print(f"You have {boxes_of_crackers} boxes of crackers!")
  print("Man that's enough for a party")
  print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("Or we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 5, 20 + 50)

print("And we can compbine both, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def home_work(a, b ,c):
    print(f"a = {a}, b = {b}, c = {c}")
home_work(1, 2, 3)

a = b = c = 3
home_work(a, b, c)
a = b = c = 3
home_work(a+1, b+2, c+3)

var1 = input("Input number 1: ")
var2 = input("Input number 2: ")
var3 = input("Input number 3: ")
home_work(var1, var2, var3)

list = [13, 14, 15]
val1 = list[0]
val2 = list[1]
val3 = list[2]
home_work(val1, val2, val3)