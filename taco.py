import copy

class Taco:
    
    def __init__(self, toppings):
        self.ingredients = copy.deepcopy(toppings)
        
    def add_sauce(self, sauce):
        self.ingredients.append(sauce)
        
default_toppings = ["Lettuce", "Tomato", "Beef"]

mild_taco = Taco(default_toppings)
hot_taco = Taco(default_toppings)
hot_taco.add_sauce("Salsa")

print(f"Hot: {hot_taco.ingredients}")
print(f"Mild: {mild_taco.ingredients}")
print(f"Default: {default_toppings}")