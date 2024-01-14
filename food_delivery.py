Count_menu_chicken = float(input())
Count_menu_fish = float(input())
Count_menu_vegan = float(input())
chicken = 10.354
fish = 12.40
vegan = 8.15
delivery = 2.5
dessert = 1.2
all_food = (Count_menu_chicken * chicken) + (Count_menu_fish * fish) + (Count_menu_vegan * vegan)
with_dessert = ((all_food * 1.2) - all_food)
Total = ((all_food + with_dessert) + delivery)
print(Total)
