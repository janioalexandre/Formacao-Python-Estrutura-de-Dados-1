from array import array

print("Hello, World!")

# Vetores

vetores_inteiros = array('b', [1, 2, 3])
print(vetores_inteiros)

vetores_inteiros.insert(3, 4)
print(vetores_inteiros)

print(vetores_inteiros.index(2))