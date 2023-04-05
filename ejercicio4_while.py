#Imprima los n números primos contenidos en un intervalo (por ejemplo los números primos del 1 al 10)

n = int(input("Ingrese el valor inicial del intervalo: "))
a = int(input("Ingrese el valor final del intervalo: "))

while n <= a:
  divisores = 1
  primos = 0
  while divisores <= a:
    if n % divisores == 0:
      primos = primos + 1
    divisores = divisores + 1
  if primos == 2:
    print(n)
  n = n + 1