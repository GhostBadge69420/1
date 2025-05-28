def print_address(**kwargs):
    for value in kwargs.values():
        print(value)

print_address(street="123 Fake St.", 
              city="Detroit", 
              state="MI", 
              zip="54321")