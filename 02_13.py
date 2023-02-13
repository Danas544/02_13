squares = [number * number for number in range(10)]
print(squares)


squares = []
for number in range(10):
    squares.append(number * number)
print(squares)


squares = {i: i * i for i in range(10)}
print(squares)



values = ["a", "b", "c"]
for index, value in enumerate(values, start=1):
    print(index, value)