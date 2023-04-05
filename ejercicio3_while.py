#Dados dos numeros, determine el MCD (Maximo Común Divisor) entre ellos.

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

a = num1 % num2
b = num2 % a
c = a % b
i = 0

while i <= num1 and i <= num2:
  if c == 0:
    print(b)
    break
    continue
  elif c != 0:
    print(c)
    break