toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)

print("We sell ", num_pizzas, " different kinds of pizza!")

sorted_toppings = sorted(toppings)
print(sorted_toppings)

sorted_prices = sorted(prices)
print(sorted_prices)


pizzas = list(zip(prices, toppings))

print(pizzas)

sorted_pizzas = pizzas.sort()

print(tuple(pizzas))

cheapest_pizza = pizzas[0]

priciest_pizza = pizzas[-1]

three_cheapest = pizzas[:3]

print(three_cheapest)

num_two_dollar_slices = prices.count(2)

print(num_two_dollar_slices)




