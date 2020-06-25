def ground_shipping(weight):
    if weight <= 2:
        price = weight * 1.50 + 20
    elif 2 < weight <= 6:
        price = weight * 3.00 + 20
    elif 6 < weight <= 10:
        price = weight * 4.00 + 20
    else:
        price = weight * 4.75 + 20
    return price


print (ground_shipping (4))

premium_ground_shipping = 125.00


def drone_shipping(weight):
    if weight <= 2:
        price = weight * 4.50
    elif 2 < weight <= 6:
        price = weight * 9.00
    elif 6 < weight <= 10:
        price = weight * 12.00
    else:
        price = weight * 14.25
    return price


print (drone_shipping (1.5))


def find_cheapest(weight: object) -> object:
    if ground_shipping (weight) < drone_shipping (weight) and ground_shipping (weight) < premium_ground_shipping:
        return "better go with ground shipping"
    elif drone_shipping (weight) < ground_shipping (weight) and drone_shipping (weight) < premium_ground_shipping:
        return "give it to the drone,my man"
    else:
        return "premium ground shipping is the way to go"


print (find_cheapest (80))
