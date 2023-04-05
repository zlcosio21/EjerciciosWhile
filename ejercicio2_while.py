#De los n elementos de la seria de Fibonacci diga cuantos son pares y cuantos impares.

n = int(input("Ingrese cuantos elementos tendrá la serie de Finobacci: "))

num1 = 0
num2 = 1
i = 1
pares = 0
impares = 0

while i <= n:
  print(f"Fib{i} = {num2}")
  num1, num2 = num2, num1 + num2
  i += 1
  if num2 % 2 == 0:
    pares += 1
  else:
    impares += 1

print(f"Hay {pares} numeros pares")
print(f"Hay {impares} numeros impares")