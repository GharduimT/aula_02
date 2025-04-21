Exec01= "Exercício 1" #nesse caso como há necessidade de calculo poderia usar tanto int quanto float#
print(Exec01)
#entrada
numero = int (input('digite um número de 1 a 10: '))

#processamento
num_anterior = (numero - 1)
num_posterior = (numero +1)

#saída
print('O número anterior ao seu é:', num_anterior, "e o núemero posterior é: ", num_posterior, "logo seu número é:",numero,)
"\n"

# titulo
Exec02 = "Exercício 2"
enunciado2 = "Crie um programa que leia um número apresente o seu dobro, o tríplo e o seu valor elevado ao quadrado"
print(Exec02, "\n", enunciado2,)


#processamento
numero = int (input('digite um número de 1 a 10: '))
dobro = (numero*2)
triplo = (numero*3)
quadrado = (numero*numero)#numero ** 2#

print('Seu número escolhido foi: ', numero,"\n" 'Portanto o dobro desse número é: ', dobro, "\n" 'O triplo é: ', triplo,"\n"
      'E valor do seu número elevado ao quadrado é: ', quadrado,)
"\n"
Exec03= 'Exercicio 3'
enunciado3 = "Faça um programa que converta centímetros em milímetros"
print(Exec03, "\n", enunciado3,)

#entrada
metro = int(input('Informe a medida em metros: '))

#processamento
centimetros = metro * 100
milímetros = metro * 1000

print("Centímetros", centimetros)
print("Milímetros", milímetros)

