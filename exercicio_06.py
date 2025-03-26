dicionario_1 = {"a": 2, "b": 3, "c": 5}
dicionario_2 = {"a": 1, "b": 4, "d": 7}

# resolver passando a Para combinar dois dicionários em Python, pode usar o operador de mesclagem (|), o operador de descompactação (**) ou a função dict()

def combina_dicionarios(*dicionarios): # função que recebe *dicionários como parâmetro e por meio do *dicionarios e retorna um novo dicionário com as chaves e valores combinados. 
    novo_dicionario = {} # dicionário vazio para armazenar a soma dos valores dos dicionários
    for dicionario in dicionarios:
        for chave, valor in dicionario.items(): # para cada chave, valor no dicionario executa o bloco de código abaixo
            novo_dicionario[chave] = novo_dicionario.get(chave, 0) + valor # soma o valor da chave no novo dicionário, caso a chave já exista no dicionário, soma o valor da chave com o valor atual, se não existe usa o get para garantir que comece do zero antes de somar.
    return novo_dicionario

print(combina_dicionarios(dicionario_1, dicionario_2))





# def combina_dicionarios(dicionario_1, dicionario_2): # função que recebe os dois dicionarios como parâmetro.
#     resultado = {} # variavel que irá armazenar o resultado da função, inicialmente vazia.
#     for chave in dicionario_1: # para cada chave no dicionario_1 executa o bloco de código abaixo.
#         if chave in dicionario_2:
#             resultado[chave] = dicionario_1[chave] + dicionario_2[chave] # resultado[], pega o valor da chave no dicionario_1 e soma com o valor da chave no dicionario_2 e armazena na variavel resultado.
#         else: # se a chave não estiver no dicionario_2, adiciona o valor da chave no dicionario_1 na variavel resultado.
#             resultado[chave] = dicionario_1[chave]
#     for chave in dicionario_2: 
#         if chave not in resultado: # se a chave não estiver no resultado, adiciona o valor da chave no dicionario_2 na variavel resultado, assim a chave que está no 2 e não está no 1, como "d" será adicionada no resultado.
#             resultado[chave] = dicionario_2[chave]
#     return resultado
# print(combina_dicionarios(dicionario_1, dicionario_2))

