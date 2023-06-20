from blueprints.classes.validacao import validacao
from ext.banco_dados import conexaoBanco


class volte(validacao):

    def __init__(self, telefoneA='', telefoneB='', ddd_registrado='',bo='', rn='', rop=''):
        super().__init__(telefoneA, telefoneB, ddd_registrado, bo, rn, rop)
        
    def TctdiVolte(self):
        #  Compara o DDD da origem com o DDD do destino
        prefixo_A_igual_B = self.telefoneA[0:2] == self.telefoneB[0:2]             
        Telefone_validoA, Telefone_validoB = self.TelefoneSemCaracterEspecial()

        if Telefone_validoB[0] == '+':
            return self.retornoVolte(formato_chamada='0041', 
                                     regiao_chamada=self.telefoneA[0])

        if self.telefoneB[0:4] == '0800' and self.ddd_registrado != '':
            return self.retornoVolte(formato_chamada='041', 
                                     regiao_chamada=self.ddd_registrado[0])
        
        if self.telefoneB[0:4] == '0800' and self.ddd_registrado == '':
            return self.retornoVolte(formato_chamada='0', 
                                     regiao_chamada=self.telefoneA[0])

        #  Verifica se o DDD do telefone A é igual do B, 
        #  e se o DDD registrado não foi preenchido, então ligação local 
        if prefixo_A_igual_B is True and self.ddd_registrado == '':
            return self.retornoVolte(formato_chamada='0', 
                                     regiao_chamada=Telefone_validoB[0])
        
        #  Verifica se o DDD do telefone A é igual do B, 
        #  e se o DDD registrado foi preenchido, com o mesmo DDD
        #  da origem, então ligação local 
        if prefixo_A_igual_B is True and self.ddd_registrado == self.telefoneA[0:2]:
            return self.retornoVolte(formato_chamada='0', 
                                     regiao_chamada=Telefone_validoB[0])
        
        #  Verifica se o DDD do telefone A é diferente do B, se for ligação é LD 
        if prefixo_A_igual_B is False:
            return self.retornoVolte(formato_chamada='041', 
                                     regiao_chamada=Telefone_validoB[0])
        
        #  Verifica se o DDD do telefone A é igual do B, e se o DDD registrado é 
        #  igual ao DDD da origem, se não for a ligação é LD 
        if prefixo_A_igual_B is True and self.ddd_registrado != self.telefoneA[0:2]:
            return self.retornoVolte(formato_chamada='041', 
                                     regiao_chamada=Telefone_validoB[0])

        
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
    
    def retornoVolte(self, formato_chamada, regiao_chamada):
        Telefone_validoA, Telefone_validoB = self.TelefoneSemCaracterEspecial()

        if Telefone_validoB[0] == '+':
            Telefone_validoB = Telefone_validoB[1:]
        
        contador = 0
        for tupla in self.getDB():            
            if tupla[0][0] == regiao_chamada:
                regiao, site1, site2, bo1, bo2, bnt = self.getDB()[contador]

                if regiao == '4X' or regiao == '8X':
                    formato1 = f'{site1}\ntctdi:bo={bo1}, bnt={bnt}, anb={Telefone_validoA}, bnb={formato_chamada} {self.conversaoRN()} {self.rop} {Telefone_validoB}, cl=1;'
                    formato2 = f'{site2}\ntctdi:bo={bo2}, bnt={bnt}, anb={Telefone_validoA}, bnb={formato_chamada} {self.conversaoRN()} {self.rop} {Telefone_validoB}, cl=1;'
                    return f'{formato1}\n\n{formato2}'
                
                if regiao =='5X':
                    return f'{site1}\ntctdi:bo={bo1}, bnt={bnt}, anb={Telefone_validoA}, bnb={formato_chamada} {self.conversaoRN()} {self.rop} {Telefone_validoB}, cl=1;'
                
                if regiao[0] == '9':
                    return self.retornoRegiao9x(formato_chamada)
                
                formato1 = f'{site1}\ntctdi:bo={bo1}, bnt={bnt}, anb={Telefone_validoA}, bnb={formato_chamada} {self.conversaoRN()} {self.rop} {Telefone_validoB}, cl=1;'
                formato2 = f'{site2}\ntctdi:bo={bo1}, bnt={bnt}, anb={Telefone_validoA}, bnb={formato_chamada} {self.conversaoRN()} {self.rop} {Telefone_validoB}, cl=1;'
                return f'{formato1}\n\n{formato2}'
            contador += 1
    
                
    def retornoRegiao9x(self, formato_chamada):
        Telefone_validoA, Telefone_validoB = self.TelefoneSemCaracterEspecial()        
        contador = 0
        for tupla in self.getDB():            
            if tupla[0] == self.telefoneB[0:2]:
                _, site1, _, bo1, _, bnt = self.getDB()[contador]
                return f'{site1}\ntctdi:bo={bo1}, bnt={bnt}, anb={Telefone_validoA}, bnb={formato_chamada} {self.conversaoRN()} {self.rop} {Telefone_validoB}, cl=1;'
            contador += 1    

    def __str__(self) -> str:
        return self.TctdiVolte()    

    
