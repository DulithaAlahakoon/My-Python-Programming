class Ceylon:
  def capital(self):
    print("Kotte is the capital of Ceylon")

  def language(self):
    print("Sinhala is the primary language of Ceylon")

  def type(self):
    print("Small country with big rich heritage")

class UnitedKingdom:
  def capital(self):
    print("London is the capital of United Kingdom")

  def language(self):
    print("English is the primary language of United Kingdom")

  def type(self):
    print("Countrys with big rich heritage")

sl = Ceylon()
uk = UnitedKingdom()

for country in (sl, uk):
  country.capital()
  country.language()
  country.type()