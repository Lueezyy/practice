totC = 1800
totP = 180
m = 3

p = 180 / m
c = 1800 / m

chickenProtein = 25 / 112
chickenCalories = 140 / 112
chickenServings = p / chickenProtein
chickenTotCalories = chickenServings * chickenCalories
chickenTotProtein = chickenServings * chickenProtein

riceProtein = 4 / 45
riceCalories = 160 / 45
riceServings = (c - chickenTotCalories) / riceCalories
riceTotCalories = riceServings * riceCalories
riceTotProtein = riceServings * riceProtein

print(f"Chicken servings: {chickenServings:.0f} grams.")
print(f"Chicken calories and protein: {chickenTotCalories:.0f} {chickenTotProtein:.0f}")
print(f"\nRice servings: {riceServings:.0f} grams.")
print(f"Rice calories and protein: {riceTotCalories:.0f} {riceTotProtein:.0f}")
print(f"\nMeal calories and protein: {(chickenTotCalories + riceTotCalories):.0f} {(chickenTotProtein + riceTotProtein):.0f}")