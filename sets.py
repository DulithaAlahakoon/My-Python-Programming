days = {"mon", "tue", "wed", "thu", "fri", "sat", "sun"}
print(days)
print(type(days))

days.add("funday")
print(days)

days.update (["fuckday", "suckday", "blowday"])
print(days)

days.discard("suckday")
print(days)

days.remove("blowday")
print(days)

setx = {"apple", "banana", "cherry"}
for x in setx:
  print(x)


set1 = {"ford", "honda", "toyota", "nissan"}
set2 = {"jeep", "bmw", "cat", "ford", "honda"}

print(set1.union(set2))
print(set1 | set2)

print(set1 & set2)