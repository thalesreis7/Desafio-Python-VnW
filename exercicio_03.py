lista_de_linguagens = ["Java", "Java", "Ruby", "Javascript", "Ruby"]

def vezes_aparece(lista_de_linguagens): ## função que recebe uma lista de linguagens
    contagem = {} # dicionário vazio para armazenar a contagem das linguagens
    for linguagem in lista_de_linguagens: # para cada linguagem na lista_de_linguagens executa o bloco de código abaixo
        if linguagem in contagem: # se a linguagem já está no dicionário adiciona 1 ao valor da linguagem, se não adiciona a linguagem no dicionário recebe o valor de 1
            contagem[linguagem] += 1 
        else:
            contagem[linguagem] = 1
    return contagem

print(vezes_aparece(lista_de_linguagens))