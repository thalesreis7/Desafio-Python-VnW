medias_alunos = {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]} # dicionário com as notas dos alunos

def calc_notas(medias_alunos): # função que recebe um dicionário com as notas dos alunos e retorna uma lista de tuplas com o nome do aluno e sua média
    lista_tuplas = [] # lista vazia para armazenar as tuplas com o nome do aluno e sua média
    for aluno, notas in medias_alunos.items(): # para cada aluno e suas notas no dicionário executa o bloco de código abaixo
        media = sum(notas) / len(notas) # calcula a média das notas do aluno.
        arredondamento = round(media, 2) # arredonda a média para 2 casas decimais
        tuple = (aluno, arredondamento) # cria uma tupla com o nome do aluno e sua média
        lista_tuplas.append(tuple) # adiciona a tupla na lista de tuplas 
    return lista_tuplas # retorna a lista de tuplas com o nome do aluno e sua média
print(calc_notas(medias_alunos)) # imprime a lista de tuplas com o nome do aluno e sua média