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

        #  Valida se o ROP e o RN foram preenchidos com cinco digitos
        #  ou se utilizaram espaço para preencher'''
        validacao_rn = self.rn.strip() != '' and len(self.rn) == 5
        validacao_rop = self.rop.strip != '' and len(self.rop) == 5

        #  Compara o DDD da origem com o DDD do destino
        prefixo_A_igual_B = self.telefoneA[0:2] == self.telefoneB[0:2]

        if validacao_rn is False or validacao_rop is False:
            return 'Verifique RN/ROP'

        if self.ddd_registrado != '':
            return 'Cliente não pode usar fora da Home Zone'     

        if self.ddd_registrado == '' and prefixo_A_igual_B is True:
            #  Campo ddd_registrado em branco e A é igual ao de B, chamada local
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb={rn_valido} {self.rop} {Telefone_validoB[2:]}, ea={Telefone_validoA[0:2]}, cl=1, tmr=0;'

        if self.ddd_registrado == '' and prefixo_A_igual_B is False:
            #  Campo ddd_registrado em branco e o DDD de A é diferente do de B, chamada LD
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb={rn_valido} {self.rop} 041{Telefone_validoB}, ea={Telefone_validoA[0:2]}, cl=1, tmr=0;'

           
    
    def __str__(self) -> str:
        return self.TctdiFixo()