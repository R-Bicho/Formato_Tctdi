from blueprints.classes.validacao import validacao

class telefoneMovel(validacao):
    def __init__(self, telefoneA='', telefoneB='', ddd_registrado='', bo='', tipo_chamada =''):
        super().__init__(telefoneA, telefoneB, ddd_registrado, bo)
        self.tipo_chamada = tipo_chamada

    def TctdiMovel(self) -> str:
        Telefone_validoA, Telefone_validoB = self.TelefoneSemCaracterEspecial()
        
        prefixo_A_igual_B = self.telefoneA[0:2] == self.telefoneB[0:2]

        if self.tipo_chamada == 'pos':
            valor_CL = '1'
        else:
            valor_CL = '4'

        #  --Retorna comando para chamadas internacionais
        if Telefone_validoB[0] == '+' and self.ddd_registrado == '':
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb=0041 {Telefone_validoB[1:]}, ea={Telefone_validoA[0:2]}, cl={valor_CL};'
        
        if Telefone_validoB[0] == '+' and self.ddd_registrado != '':
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb=0041 {Telefone_validoB[1:]}, ea={self.ddd_registrado}, cl={valor_CL};'

        #  --Retorna comando para chamadas 0800
        if self.ddd_registrado == '' and Telefone_validoB[0:4] == '0800':
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb={Telefone_validoB}, ea={Telefone_validoA[0:2]}, cl={valor_CL};'
        
        if self.ddd_registrado != '' and Telefone_validoB[0:4] == '0800':
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb={Telefone_validoB}, ea={self.ddd_registrado}, cl={valor_CL};'

        #  --Retorna comando para chamadas nacionais
        if self.ddd_registrado == '' and prefixo_A_igual_B is True:
            #  Campo ddd_registrado em branco e DDD A é igual ao de B, chamada local
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb={Telefone_validoB[2:]}, ea={Telefone_validoA[0:2]}, cl={valor_CL};'

        if self.ddd_registrado == '' and prefixo_A_igual_B is False:
            #  Campo ddd_registrado em branco e o DDD de A é diferente do de B, chamada LD
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb=041{Telefone_validoB}, ea={Telefone_validoA[0:2]}, cl={valor_CL};'

        if self.ddd_registrado != '' and prefixo_A_igual_B is True and (self.ddd_registrado == self.telefoneA[0:2]):
            #  Campo ddd_registrado preenchido e valor digitado é igual ao DDD
            #  cadastrado da origem, chamada local
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb={Telefone_validoB[2:]}, ea={Telefone_validoA[0:2]}, cl={valor_CL};'

        if self.ddd_registrado != '' and prefixo_A_igual_B is True and (self.ddd_registrado != self.telefoneA[0:2]):
            #  Campo ddd_registrado preenchido e o numero digitado é diferente
            #  do DDD cadastrado, chamada é LD
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb=041{Telefone_validoB}, ea={self.ddd_registrado}, cl={valor_CL};'
        
        if self.ddd_registrado != '' and prefixo_A_igual_B is False:
            #  Campo ddd_registrado preenchido e o numero digitado é diferente
            #  do DDD cadastrado, chamada é LD
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb=041{Telefone_validoB}, ea={self.ddd_registrado}, cl={valor_CL};'
        return 'erro inesperado'
    
    def __str__(self) -> str:
        return self.TctdiMovel()