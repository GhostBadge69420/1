temp = 0
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny")
elif temp <=0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif temp < 28 and temp > 0 and is_sunny:
    print("Its warm outside")
    print("It is sunny")
    