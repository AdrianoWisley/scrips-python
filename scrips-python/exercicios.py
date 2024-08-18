#crie uma função q imprime a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e
#depois faça uma chamada á função para lista os números
'''def listaPar():
    for i in range(2, 21, 2):
        print(i)
listaPar()'''

#crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2
#elementos a lista e imprima a lista
'''def listaString(texto):
    print(texto.upper())
    return
listaString('Rumo à análizene de Dados')'''

#crie uma função que recebe como parâmetro um alista de 4 elementos, adicione 2
#elementos a lista e imprima a lista
'''def novaLista(lista):
    print(lista.append(5))
    print(lista.append(6))
    
lista1 = [1, 2, 3, 4]
novaLista(lista1)
print(lista1)'''

#crie uma função que receba um argumento formal e uma possível lista de elementos.
#faça dus chamadas á função com apenas 1 elemento e na segunda com 4 elementos.
'''def printNum( arg1, *lista ):
    print (arg1)
    for i in lista:
        print (i)
    return;
#chama à função
printNum( 100 )
printNum( 'A', 'B', 'C')'''

#crie uma função anônima e atribua seu retorno a uma variavel chamada soma. Aexpressão vai
#recer 2 números como parâmetro e retornar a soma deles.
'''soma = lambda arg1, arg2: arg1 + arg2
print ('a soma é : ', soma(452, 298))'''

#Execute o cógigo abaixo e certifique-se que compreende a diferença entre variavel global e local.
'''total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2;
    print ('Dentro da função o total é: ', total)
    return total;

soma(10, 20 );
print('fora da função o total é: ', total)'''

#crie uma função anônima que converta cada temperatura para fahrenheit.
'''Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print(list(Fahrenheit))'''

#crie um estrutura que pergunte ao usuário qual o dia da semana. se o dia for igual a Domingo ou
#igual a sábado, imprima na tela "hoje é dia de descanso", caso contrário imprima na tela "você precisa trabalha1".
'''dia = input('Digite o dia da semana ')
if dia == 'Domingo' or dia == 'Sábado':
    print('Hoje é dia de descando')
else:
    print('Você precisa trabalha!')'''


#crie uma lista de 5 frutas e verifique se a fruta 'morango' faz parte da lista.
'''lista = ['laranja', 'Maça', 'Uva', 'Morango']
for fruta in lista:
    if fruta == 'Morango':
        print("Morango faz parte da lista de frutas")'''


#crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma lista.
'''tup1 = (1, 2, 3, 4)
lst1 = []
for i in tup1:
    novo_valor = i * 2
    lst1.append(novo_valor)
print(lst1)'''

#crie uma sequência de número pares entre 100 e 150 e imprima na tela.
'''for i in range(100, 151, 2):
    print(i)'''

#crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35,
#imprima as temperaturas na tela.
'''temperatura = 40
while temperatura > 35:
    print(temperatura)
    temperatura = temperatura - 1'''

#crei uma variável chmada contador = 0. Enquanto couter for menor que 100, imprima os valores na tela,
#mas qquando for encontrado o valor 23, interrompa a execução  do programa.
'''contador = 0
while contador < 100:
    if contador == 23:
        break
    print(contador)
    contador += 1'''

#crie uma lista vazia e uma variavel com valor 4. Enquanto o valor da variável for menor ou iqual a 20,
#adicione à lista, apenas os valores pares e imprema a lista.
'''numeros = list()
i = 4
while (i <= 20):
    numeros.append(i)
    i = i+2
print(numeros)'''

#transforme o resultado desta função range em uma lista: range(5, 45, 2)
'''nums = range(5, 45, 2)
print(list(nums))'''

#Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros
'''temperatura = int(input('Qual a temperatura? '))
if temperatura >= 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')'''

#Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. use um placeholder na sua instrução de impressão
frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
count = 0
for caracter in frase:
    if caracter == 'r':
        count += 1
print('O caracter r aparece {} vezes na frase.'.format(count))

    


    

    

    
    










