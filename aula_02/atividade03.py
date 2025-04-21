#titulo
enunc = "IMPLEMENTE UM ALGORÍRIMO QUE LEIA AS NOTAS DE TESTE E DA PROVA DE UM ALUNO, RETIRE A MÉDIA E MOSTRE O RESULTADO NA TELA"
exec1 = "Exercício 1"

print(exec1)
print(enunc) 
"\n"

nota_teste = int(input ('Digite aqui a nota do teste: '))
nota_prova = int(input ('Digite aqui a nota da prova:  '))

total = (nota_teste + nota_prova)
media = (total/2)
#)processamento
print ("a média das notas é:", media)