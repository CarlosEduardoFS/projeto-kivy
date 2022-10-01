class Imc:
    PERCENTUAL_GORDURA_HOMEM_JOVEM = [8,22]
    PERCENTUAL_GORDURA_MULHER_JOVEM = [20,35]
    PERCENTUAL_GORDURA_HOMEM_ADULTO = [15,19]
    PERCENTUAL_GORDURA_MULHER_ADULTO = [15,30]
    
    @staticmethod
    def calcular_imc(peso,altura):
        return peso/(altura * altura)