def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.", 
              city="Detroit", 
              state="MI", 
              zip="54321")