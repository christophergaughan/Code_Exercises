from collections import defaultdict
# This allows you to populate a dictionary with many keys but leave an empty value 
# and the empty value can be any of the python objects i.e. str, list, dict etc.
# we'll make a dice object and keep track of the value of the rolls
dice = defaultdict(int)
# print(dice)
for i in range(2,13):
    dice[i]
    
print(dice)
    
# here we'll group data with defaultdict 
import random
names = ["Liam", "Olivia", "Noah", "Emma", "William",
         "Ava", "James", "Isabella"]
countries = ["US", "UK", "China", "Russia", "France"]
data = [(random.choice(countries), random.choice(names)) for i in range(10)]
print(data)

grouped = defaultdict(list)
for country, name in data:
    grouped[country].append(name)
print(grouped)                                                                                                                           