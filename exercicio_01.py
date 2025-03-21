lista_de_num = [2,4,10,3,9,7,15,22] #lista de números inteiros

def soma_pares(lista_de_num): # função que irá somar os números inteiros recebendo a lista como parâmetro
    soma = 0 # variável que irá armazenar a soma dos números pares  
    for num in lista_de_num: # loop for que irá percorrer cada número da lista
        if num % 2 == 0: # condicional if que verifica se o resto da divisão do numero por 2 é zero
            soma +=  num # se a condição for verdadeira, o número é par e é adicionado a variável soma
    return soma # retorna a soma final de todos os numeros pares
print(f"A soma dos pares é: {soma_pares(lista_de_num)}") # mostra no terminal o resultado da soma, chamando a função e imprimindo o resultado
        
    