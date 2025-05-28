# display street an apartment, but the user doesn't have an apartment?

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
    
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state') }, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               apt="#100",
               city="Detroit",
               state="MI",
               zip="54321")