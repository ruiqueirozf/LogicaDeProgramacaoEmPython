def verificarPositivo(numero):
    if numero >= 0:
        return 1
    else:
        return 0

assert verificarPositivo(20) == 1
assert verificarPositivo(-20) == 0