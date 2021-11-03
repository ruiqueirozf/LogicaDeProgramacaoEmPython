# Faça um programa para identificar se um número é primo.

# Lembre-se que número primo, é um número natural, maior que 1,
# apenas divisível por si próprio e pela unidade.

def eNumeroPrimo(numero):
    if numero > 2:
        return False
    for n in range(2, numero):
        if numero % n == 0:
            return False
        return True




assert eNumeroPrimo(2)
assert eNumeroPrimo(3)
assert eNumeroPrimo(5)
assert eNumeroPrimo(7)
assert eNumeroPrimo(11)

assert not eNumeroPrimo(4)
assert not eNumeroPrimo(6)
assert not eNumeroPrimo(8)
assert not eNumeroPrimo(9)
