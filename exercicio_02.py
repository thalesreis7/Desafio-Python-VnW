pessoas = ( ("Samuel", 20), ("Karynne", 19), ("Carol", 22), ("Kleber", 25), ("Vinicius", 21))

def ordenacao(pessoas):
    pessoas = sorted(pessoas , key=lambda x: x[1])# ordena a lista de tuplas pela idade, passando a key como parâmetro para a função sorted, o x é a variável auxiliar da função lambda, x[1] pega o segundo elemento da tupla, que é a idade.
    return pessoas
print(ordenacao(pessoas))