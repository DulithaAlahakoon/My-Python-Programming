car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car)

for x in car:
  print(x, car[x])

print(car.keys())
print(car.values())

x = car["model"]
print(x)

dic = {}

dic["name"] = "Dulitha"
dic["age"] = 26
dic["city"] = "Mawathagama"

print(dic)

dic.pop("name")
print(dic)
del dic["city"]
print(dic)
del dic