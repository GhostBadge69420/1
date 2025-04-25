price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:.2f}") # 2 amount of decimals "f" means floating number
print(f"Price 1 is ${price2:.2f}")
print(f"Price 1 is ${price3:.2f}")

print(f"Price 1 is ${price1:.3f}")
print(f"Price 1 is ${price2:.3f}")
print(f"Price 1 is ${price3:.3f}")

print(f"Price 1 is ${price1:10}") #to allocate space add number "10"
print(f"Price 1 is ${price2:10}")
print(f"Price 1 is ${price3:10}")

print(f"Price 1 is ${price1:010}") # zero padding
print(f"Price 1 is ${price2:010}")
print(f"Price 1 is ${price3:010}")

print(f"Price 1 is ${price1:<10}") #left justify
print(f"Price 1 is ${price2:<10}")
print(f"Price 1 is ${price3:<10}")

print(f"Price 1 is ${price1:>10}") # right justify
print(f"Price 1 is ${price2:>10}")
print(f"Price 1 is ${price3:>10}")

print(f"Price 1 is ${price1:^10}") # center align
print(f"Price 1 is ${price2:^10}")
print(f"Price 1 is ${price3:^10}")

print(f"Price 1 is ${price1:+}") # +ve value
print(f"Price 1 is ${price2:+}")
print(f"Price 1 is ${price3:+}")

print(f"Price 1 is ${price1: }") # space
print(f"Price 1 is ${price2: }")
print(f"Price 1 is ${price3: }")

print(f"Price 1 is ${price1:,}") # thousand separator
print(f"Price 1 is ${price2:,}")
print(f"Price 1 is ${price3:,}")

print(f"Price 1 is ${price1:+,.2f}") # +ve sign,separator and 2 decimal point
print(f"Price 1 is ${price2:+,.2f}")
print(f"Price 1 is ${price3:+,.2f}")
