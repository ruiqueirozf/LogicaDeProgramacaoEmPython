def verificarParOuImpar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

assert verificarParOuImpar(2)
assert not verificarParOuImpar(10)