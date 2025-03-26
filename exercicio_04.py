string = "banana maçã banana laranja maçã maçã"

def contagem(string): 
    dicionario = {} # dicionário vazio para armazenar a contagem das palavras
    lista = string.split(', ') # separa a string em uma lista de palavras
    for item in lista:
        if not item in dicionario.keys(): # se o item não está no dicionário, adiciona o item no dicionário e a quantidade de vezes que aparece na lista
            dicionario[item] = lista.count(item)
    return dicionario

print(contagem(string))
        
            