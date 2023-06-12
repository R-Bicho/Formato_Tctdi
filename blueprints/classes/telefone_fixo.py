from blueprints.classes.validacao import validacao


class telefoneFixo(validacao):

    def __init__(self, telefoneA='', telefoneB='', ddd_registrado='', bo='', rn='', rop=''):
        super().__init__(telefoneA, telefoneB, ddd_registrado, bo, rn, rop)

    def TctdiFixo(self) -> str:
        '''
        Metodo criado para validar se o numero é fixo e retornar o TCTDI no
        formato correto de acordo com a solicitação do usuario
        '''

        Telefone_validoA, Telefone_validoB = self.TelefoneSemCaracterEspecial()

        rn_valido = self.rn.upper()
        #  Altera o caracter A para #10
        rn_valido = self.rn.replace('A', '#10')               
        
        #  Compara o DDD da origem com o DDD do destino
        prefixo_A_igual_B = self.telefoneA[0:2] == self.telefoneB[0:2]

        if self.bo != '445':
            return 'Selecione o campo de fixo em categoria origem'

        if self.validacaoRN() is False or self.validacaoROP() is False:
            return 'Verifique RN/ROP'        
        
        if  Telefone_validoB[0:4] == '0800':            
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb={rn_valido} {self.rop} {Telefone_validoB}, ea={Telefone_validoA[0:2]}, cl=1, tmr=0;'

        if prefixo_A_igual_B is True:
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb={rn_valido} {self.rop} {Telefone_validoB[2:]}, ea={Telefone_validoA[0:2]}, cl=1, tmr=0;'

        if prefixo_A_igual_B is False:
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb={rn_valido} {self.rop} 041{Telefone_validoB}, ea={Telefone_validoA[0:2]}, cl=1, tmr=0;'

    def __str__(self) -> str:
        return self.TctdiFixo()
