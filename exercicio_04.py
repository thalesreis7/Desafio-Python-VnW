frutas = ["banana", "maçã", "banana", "laranja", "maçã", "maçã"] #lista

def contar_palavras(frutas):# função que recebe uma string e conta quantas vezes cada palavra aparece nela
    contagem = {} # dicionário vazio para armazenar a contagem das palavras
    palavras = frutas # lista de palavras
    for palavra in palavras: # para cada palavra na lista de palavras executa o bloco de código abaixo
        if palavra in contagem: # se a palavra já está no dicionário adiciona 1 ao valor da palavra
            contagem[palavra] += 1
        else: # se a palavra não está no dicionário adiciona a palavra no dicionário com valor 1
            contagem[palavra] = 1 
    return contagem # retorna o dicionário com a contagem das palavras

print(contar_palavras(frutas)) # imprime o dicionário com a contagem das palavras