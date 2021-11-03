#Crie uma função que descubra se um valor é maior ou menor que 10.
def MaiorOuMenorQueDez(numero):
    if numero > 10:
        return True
    else:    
        return False


assert(True) == MaiorOuMenorQueDez(11)
assert(False) == MaiorOuMenorQueDez(9)