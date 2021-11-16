c = {
  'f' : 'ha',
  'g' : 'he'
}

d = [
  [32, "fuck", "suck", 'f'],
  [45, "nah", "vah", 'g']
]

for age, name, surname, g in d:
  a = f"{age}, {name}, {surname}, {c[g]}"
  print (a)