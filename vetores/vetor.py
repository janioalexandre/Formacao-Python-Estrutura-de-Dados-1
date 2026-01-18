class Vetor:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.__posicao = 0

    def inserir_elemento_posicao(self, elemento, posicao):
        vetor_inicio = self.__elementos[:posicao] + [None]
        vetor_final = self.__elementos[posicao:]
        vetor_inicio[len(vetor_inicio) - 1] = elemento
        self.__elementos = vetor_inicio + vetor_final
        self.__posicao += 1

    def inserir_elemento_final(self, elemento):
        if self.__posicao >= len(self.__elementos):
            self.__elementos = self.__elementos + [None]
        
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def listar_elementos(self, posicao):
        return self.__elementos[posicao]
