


num_inicial = int(input('Digite o numero inicial do intervalo: '))
num_final = int(input('Digite o numero final do intervalo: '))

soma_pares = 0

for num in range(num_inicial, num_final + 1):
    if num % 2 == 0:
        soma_pares += num

if soma_pares > 0:
    print(f'A soma dos números pares no intervalo de {num_final} a {num_final} é: {soma_pares}')
else:
    print('Não há números pares no intervalo.')
