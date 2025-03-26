lista_de_linguagens = "Java, Java, Ruby, Javascript, Ruby"

def frequencia(lista_de_linguagens): ## função que recebe uma lista de linguagens
    contagem = {} # dicionário vazio para armazenar a contagem das linguagens
    lista = lista_de_linguagens.split(', ') # separa a string em uma lista de linguagens
    for item in lista: 
        if not item in contagem.keys(): # se o item não está no dicionário, adiciona o item no dicionário e a quantidade de vezes que aparece na lista
            contagem[item] = lista.count(item)
    return contagem

print(frequencia(lista_de_linguagens))