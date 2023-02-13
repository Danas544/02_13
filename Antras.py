#Create a dictionary with 5 kay:value pairs, Keys must be strings, values must be numbers double digits(int)
# Use dictionary comprehension to create a new dictionary where keys are the same keys as your currents ones just all cappital letters, 
# and values are in reverse order. (25 -> 52)



# squares = {i: i * i for i in range(10)}
# print(squares)

a = {
    "Pirmas": 12,
    "Antras": 23,
    "Trecias": 34,
    "Ketvirtas": 45,
    "Penktas": 56,
}

x = {key.upper():int(str(sk)[::-1]) for key, sk in a.items()}
print(x)

