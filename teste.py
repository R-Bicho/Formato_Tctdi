from blueprints.classes.validacao import validacao
from ext.banco_dados import conexaoBanco


class volte(validacao):

    def __init__(self, telefoneA='', telefoneB='', ddd_registrado='',bo='', rn='', rop=''):
        super().__init__(telefoneA, telefoneB, ddd_registrado, bo, rn, rop)
         
        print(self.TctdiVolte())  
        for valor in self.getDB():
            print(valor)
               
    def TctdiVolte(self):
        #  Compara o DDD da origem com o DDD do destino
        prefixo_A_igual_B = self.telefoneA[0:2] == self.telefoneB[0:2]  

        if self.validacaoTelefone() == False:
            return 'Digite um Telefone Válido'    
      
        #  Verifica se o DDD do telefone A é igual do B, 
        #  e se o DDD registrado não foi preenchido, então ligação local 
        if prefixo_A_igual_B is True and self.ddd_registrado == '':
            return self.regiaoLocal()
        
        #  Verifica se o DDD do telefone A é igual do B, 
        #  e se o DDD registrado foi preenchido, com o mesmo DDD
        #  da origem, então ligação local 
        if prefixo_A_igual_B is True and self.ddd_registrado == self.telefoneA[0:2]:
            return self.regiaoLocal()
        
        #  Verifica se o DDD do telefone A é diferente do B, se for ligação é LD 
        if prefixo_A_igual_B is False:
            return self.regiaoLD()
        
        #  Verifica se o DDD do telefone A é igual do B, e se o DDD registrado é 
        #  igual ao DDD da origem, se não for a ligação é LD 
        if prefixo_A_igual_B is True and self.ddd_registrado != self.telefoneA[0:2]:
            return self.regiaoLD()

        
    def getDB(self):
        conexão = conexaoBanco()
        cur = conexão.cursor()
        cur.execute('SELECT * FROM CN_REGIOES')
        resultado = cur.fetchall()
        return resultado  
    
    def conversaoRN(self):
        rn_valido = self.rn.upper()
        #  Altera o caracter A para #10
        rn_valido = self.rn.replace('A', '#10') 
        return rn_valido
    
    def regiaoLocal(self):
        Telefone_validoA, Telefone_validoB = self.TelefoneSemCaracterEspecial()
        comparacao_regiao = Telefone_validoB[0] + 'X'

        contador = 0
        for tupla in self.getDB():            
            if tupla[0] == comparacao_regiao:
                regiao, site1, site2, bo1, bo2, bnt = self.getDB()[contador]
                formato1 = f'Site: {site1}\ntctdi:bo={bo1}, bnt={bnt}, anb={Telefone_validoA}, bnb=0 {self.conversaoRN()} {self.rop} {Telefone_validoB}, cl=1;'
                formato2 = f'Site: {site2}\ntctdi:bo={bo1}, bnt={bnt}, anb={Telefone_validoA}, bnb=0 {self.conversaoRN()} {self.rop} {Telefone_validoB}, cl=1;'
                return f'{formato1}\n\n{formato2}'
            contador += 1
    
    def regiaoLD(self):
        Telefone_validoA, Telefone_validoB = self.TelefoneSemCaracterEspecial()
        comparacao_regiao = self.telefoneB[0] + 'X'
        contador = 0
        for tupla in self.getDB():            
            if tupla[0] == comparacao_regiao:
                regiao, site1, site2, bo1, bo2, bnt = self.getDB()[contador]
                formato1 = f'Site: {site1}\ntctdi:bo={bo1}, bnt={bnt}, anb={Telefone_validoA}, bnb=041 {self.conversaoRN()} {self.rop} {Telefone_validoB}, cl=1;'
                formato2 = f'Site: {site2}\ntctdi:bo={bo1}, bnt={bnt}, anb={Telefone_validoA}, bnb=041 {self.conversaoRN()} {self.rop} {Telefone_validoB}, cl=1;'
                return f'{formato1}\n\n{formato2}'
            contador += 1

            
       

valor = volte(telefoneA='1185235500',
              telefoneB='11985235500',
              rn='AA123', 
              rop='00000',
              ddd_registrado='21')       
    
    