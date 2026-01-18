from array import array
from vetores import vetor

print("Hello, World!")

# Vetores

vetores_inteiros = array('b', [1, 2, 3])
print(vetores_inteiros)

vetores_inteiros.insert(3, 4)
print(vetores_inteiros)

print(vetores_inteiros.index(2))

print(30 * "-", "Menu", 30 * "-")
print("1. Vetores")
print("2. Listas Ligadas")

menu = int(input("Digite a opção desejada: "))

if menu == 1: 
    vetor_teste = vetor.Vetor(0)
    vetor_teste.inserir_elemento_posicao(1, 0)
    vetor_teste.inserir_elemento_posicao(2, 1)

    #vetor_teste.inserir_elemento_final(1)
    #vetor_teste.inserir_elemento_final(2)
    
    print(vetor_teste.listar_elementos(0))
    print(vetor_teste.listar_elementos(1))
    
    print(vetor_teste.tamanho_vetor())
