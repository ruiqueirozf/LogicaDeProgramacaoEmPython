vetor = []
vetor = {1, 2 ,3, 4}

def somarVetor(vetor):
    soma = 0
    for num in vetor:
        soma += num
    print(soma)
    return soma

#
# Seu teste
#
vetor = [1, 2, 3, 4]
assert 10 == somarVetor(vetor)