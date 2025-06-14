def print_address(**kwargs):
    for key in kwargs.keys():
        print(key)

print_address(street="123 Fake St.", 
              city="Detroit", 
              state="MI", 
              zip="54321")