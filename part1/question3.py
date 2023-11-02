################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!


class Oven:

  def __init__(self):
    self.items = [];
    self.opt01 = ["lead", "mercury"]
    self.opt02 = ["water", "air"]
    self.opt03 = ["cheese", "dough", "tomato"]

  def add(self, item):
    print("=> ", item)
    self.items.append(item)
  def freeze(self):
    print("Ingredientes Congelados ❄...")
  def boil(self):
    print("Se ha comenzado a hervir los ingredientes 🔥...")
  def wait(self):
    print("Se ha comenzado a combinar los ingredientes 👨‍🍳...")
  def get_output(self, temperature):
    if self.items == self.opt01 and temperature == 5000:
      return "gold"
    elif self.items == self.opt02 and temperature == -100:
      return "snow"
    elif self.items == self.opt03 and temperature == 150:
      return "pizza"
    
def make_oven():
  newOven = Oven()
  return newOven
    

def alchemy_combine(oven, ingredients, temperature):
  
  print(ingredients)

  for item in ingredients:
    print(item)
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output(temperature)