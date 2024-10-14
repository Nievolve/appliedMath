def calculate_tuple(a, b):
    return (a + b, a * b, a - b)

# Får en tuple tillbaka
results = calculate_tuple(10, 4)

print("Results tuple:", results)
print("Sum:", results[0])
print("Product:", results[1])
print("Difference:", results[2])
