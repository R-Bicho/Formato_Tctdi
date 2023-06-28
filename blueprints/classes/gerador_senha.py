import random

class retornoSenha:    
    @staticmethod
    def senha_forte():

        letra = valoresSenhas.letras()
        caracter_unico = valoresSenhas.caracter_especial()
        numero = valoresSenhas.numeros()    
        senha = set()  
            
        while len(senha) != 8:
            valores_senha = [random.choice(letra), random.choice(numero),
                        random.choice(caracter_unico)]
            
            caracter_senha = random.choice(valores_senha)
            senha.add(caracter_senha)

        senha = ''.join(senha)
        return senha

    def __str__(self) -> str:
        return f'{retornoSenha.senha_forte()}'


class valoresSenhas:  
    def letras():        
        alfabeto = []
        for letra in range(ord('a'), ord('z')+1):
            alfabeto.append(chr(letra))
        return alfabeto    

    def caracter_especial():
        caracter = ['@','!', '#', '$', '%', '&']
        return caracter
    
    def numeros():
        valores = [str(x) for x in range(0,10)]
        return valores




    



    
    

    