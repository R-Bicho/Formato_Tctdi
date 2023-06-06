from blueprints.classes.validacao import validacao

class telefoneMovel(validacao):
    def __init__(self, telefoneA='', telefoneB='', ddd_registrado='', bo=''):
        super().__init__(telefoneA, telefoneB, ddd_registrado, bo)

    def TctdiMovel(self) -> str:
        Telefone_validoA, Telefone_validoB = self.TelefoneSemCaracterEspecial()

        prefixo_A_igual_B = self.telefoneA[0:2] == self.telefoneB[0:2]

        if self.ddd_registrado == '' and prefixo_A_igual_B is True:
            #  Campo ddd_registrado em branco e DDD A é igual ao de B, chamada local
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb={Telefone_validoB[2:]}, ea={Telefone_validoA[0:2]};'

        if self.ddd_registrado == '' and prefixo_A_igual_B is False:
            #  Campo ddd_registrado em branco e o DDD de A é diferente do de B, chamada LD
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb=041{Telefone_validoB}, ea={Telefone_validoA[0:2]};'

        if self.ddd_registrado != '' and prefixo_A_igual_B is True and (self.ddd_registrado == self.telefoneA[0:2]):
            #  Campo ddd_registrado preenchido e valor digitado é igual ao DDD
            #  cadastrado da origem, chamada local
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb={Telefone_validoB[2:]}, ea={Telefone_validoA[0:2]};'

        if self.ddd_registrado != '' and prefixo_A_igual_B is True and (self.ddd_registrado != self.telefoneA[0:2]):
            #  Campo ddd_registrado preenchido e o numero digitado é diferente
            #  do DDD cadastrado, chamada é LD
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb=041{Telefone_validoB}, ea={self.ddd_registrado};'
        return 'erro inesperado'
    
    def __str__(self) -> str:
        return self.TctdiMovel()