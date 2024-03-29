while True:
  try:
    x = int(input("Insert a number: "))
    break
  except ValueError:
    print("Error on insert number, please try again")


def dividir(x,y):
  try:
    resultado = x / y
    print("A resposta é: ", resultado)
  except ZeroDivisor:
    print("Divisor não pode ser zero")