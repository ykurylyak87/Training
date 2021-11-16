import ex18

x = range(6)
for i in x:
 print(i) 

a = "Hello"
print(a[2],a[4],a[2],a[4])

for x in "banana":
 print(x)
 
b = "yes of course"
print("yes" in b)

if "yes" in b:
 print("exist")

print(b[:5])


print("++++++")

a = 0
b = []

while a <= 497:
  if a % 2 == 0:
    b.append(a)
  a += 1
print(b)

print("++++++")

x = 1
a = []
b = []
c = []
while x < 100 and len(a) < 10:
    a.append(x)
    x = x + 1
else:   
    while x <= 20:
     b.append(x)
     x = x + 1
    else:
        while x <= 30:
         c.append(x)
         x = x + 1
print(a)
print(b)
print(c)

print("++++++")

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in a:
 for j in b:
   if j == i:
    c.append(j)
print(c)

c = []
for i in a:
   if i in b:
       c.append(i)
print(c)

c = []
for i in a:
   if i not in b:
    c.append(i)
print(c)

print("*" * 20)

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
#values = my_dict.values()
#print(values)
#for i in my_dict.values():
max_key = max(my_dict, key=my_dict.get)
print(max_key)

ex18.print_one("Yuriy3")