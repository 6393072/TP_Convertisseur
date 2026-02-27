def celsius_vers_fahrenheit(c):
    return (c*9/5)+32

def fahrenheit_vers_celsius(f):
    return (f-32)*5/9

def celsius_vers_kelvin(c):
    return c+273.15

def kelvin_vers_celsius(k):
    if k < 0:
        raise ValueError("Valeur infereure à zero interdite.")
    else:
        return k-273.15
