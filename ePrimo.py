
def ehPrimo(num):
    lista = []
    for n in range(1, num + 1):
       if num % n == 0:
           lista.append(n)
    if len(lista) == 2:
        return True

numUsuario = int(input('Digite um numero, para verificar se é primo!: '))

if ehPrimo(numUsuario):
    print(f'{numUsuario} É um numero primo!')
else:
    print(f'o número {numUsuario}, Não é primo')

