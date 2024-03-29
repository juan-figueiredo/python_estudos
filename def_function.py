def menorValor(lista):
  minimo = lista[0]
  for elemento in lista:
    if(elemento < minimo):
      minimo = elemento
  return minimo


lista_teste = [2, 4, 6, 7, 43, 123, 1, 45, 6]
menor =menorValor(lista_teste)
print("O menor elemento da lista é: [{}]".format(menor))