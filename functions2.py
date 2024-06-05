def name(fname, lname):
  print("Hello " + fname + " " + lname + " Kohomada ithin oyata?")
name("Dulitha","Alahakoon")


def win(*winner):
  print(winner[0] + " is the winner")

win("Dulitha", "Krishan", "Alahakoon")

def find_sum(*number):
  result = 0

  for num in number:
    result += num

  print("Sum is", result)

find_sum(1,4,5,10)

def display_val(a,b,c):
  print("value of 'a' is:", a)
  print("value of 'a' is:", b)
  print("value of 'a' is:", c)

display_val(a = "Puka", b = "kakula", c = "akmawa")


def display_info(**kid):
  print("His first name is: " + kid["fname"])

display_info(lname = "Alahakoon", fname = "Dulitha")