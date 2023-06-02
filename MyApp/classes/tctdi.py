import re


class FormatoTctdi:

    def __init__(self, telefoneA='', telefoneB='', ddd_registrado='', bo ='',
                 rn='', rop ='', pre_pago ='', pos_pago=''):
        self.telefoneA = telefoneA
        self.telefoneB = telefoneB
        self.ddd_registrado = ddd_registrado
        self.bo = bo
        self.rn = rn
        self.rop = rop   
        self.pre_pago = pre_pago
        self.pos_pago = pos_pago

        print(self.TctdiFixo())              

    def validacaoTelefone(self) -> bool:
        '''
        Expressão regular 
        '''

        telefone_regexp = re.compile(r'^([0-9]{2}) ?([0-9]{4,5})-?([0-9]{4})$')  
       
        if telefone_regexp.search(self.telefoneA) and telefone_regexp.search(self.telefoneB):
            return True
        else:
            return False 


    def TelefoneSemCaracterEspecial(self) -> tuple:
        Telefone_validoA = ''
        Telefone_validoB = ''        

        for valor in self.telefoneA:
            if valor != ' ' and valor !='-':
                Telefone_validoA += valor
        
        for valor in self.telefoneB:
            if valor != ' ' and valor !='-':
                Telefone_validoB += valor
        
        return Telefone_validoA, Telefone_validoB


    def TctdiMovel(self) -> str:
        Telefone_validoA, Telefone_validoB = self.TelefoneSemCaracterEspecial()    
        condicao = self.validacaoTelefone() == True and len(Telefone_validoA) == 11
        prefixo_A_igual_B = self.telefoneA[0:2] == self.telefoneB[0:2]

        if condicao == False:
            return 'Digite um telefone móvel valido'
        
        if self.ddd_registrado == '' and prefixo_A_igual_B == True:  
            #  Campo ddd_registrado em branco e DDD A é igual ao de B, chamada local                               
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb={Telefone_validoB[2:]}, ea={Telefone_validoA[0:2]};'            
           
        if self.ddd_registrado == '' and prefixo_A_igual_B == False:
            #  Campo ddd_registrado em branco e o DDD de A é diferente do de B, chamada LD
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb=041{Telefone_validoB}, ea={Telefone_validoA[0:2]};' 

        if self.ddd_registrado != '' and prefixo_A_igual_B == True and (self.ddd_registrado == self.telefoneA[0:2]):
            #  Campo ddd_registrado preenchido e valor digitado é igual ao DDD 
            #  cadastrado da origem, chamada local     
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb={Telefone_validoB[2:]}, ea={Telefone_validoA[0:2]};'

        if self.ddd_registrado != '' and prefixo_A_igual_B == True and (self.ddd_registrado != self.telefoneA[0:2]):
            #  Campo ddd_registrado preenchido e o numero digitado é diferente 
            #  do DDD cadastrado, chamada é LD                                   
            return f'tctdi:bo={self.bo}, anb={Telefone_validoA}, bnb=041{Telefone_validoB}, ea={self.ddd_registrado};'


    def TctdiFixo(self) -> str:
        '''
        Metodo criado para validar se o numero é fixo e retornar o TCTDI no
        formato correto de acordo com a solicitação do usuario
        '''

        Telefone_validoA, Telefone_validoB = self.TelefoneSemCaracterEspecial()

        #  Altera o caracter A para #10
        rn_valido = self.rn.replace('A','#10')     

        #  Condição para validar se o numero é de telefonia fixa
        condicao = self.validacaoTelefone() == True and len(Telefone_validoA) == 10

        #  Valida se o ROP e o RN foram preenchidos com cinco digitos
        #  ou se utilizaram espaço para preencher'''
        validacao_rn = self.rn.strip() != '' and len(self.rn) == 5
        validacao_rop = self.rop.strip != '' and len(self.rop) == 5  

        #  Compara o DDD da origem com o DDD do destino 
        prefixo_A_igual_B = self.telefoneA[0:2] == self.telefoneB[0:2]


        if condicao == False:
            return 'Digite um numero fixo válido'
        
        if validacao_rn == False or validacao_rop == False:
            return 'Verifique RN/ROP'
        
        
        if self.ddd_registrado == '' and prefixo_A_igual_B == True:  
            #  Campo ddd_registrado em branco e A é igual ao de B, chamada local                               
            return f'tctdi:bo=445, anb={Telefone_validoA}, bnb={rn_valido} {self.rop} {Telefone_validoB[2:]}, ea={Telefone_validoA[0:2]}, cl=1, tmr=0;'   

        if self.ddd_registrado == '' and prefixo_A_igual_B == False:
            #  Campo ddd_registrado em branco e o DDD de A é diferente do de B, chamada LD
            return f'tctdi:bo=445, anb={Telefone_validoA}, bnb={rn_valido} {self.rop} 041{Telefone_validoB}, ea={Telefone_validoA[0:2]}, cl=1, tmr=0;' 

        if self.ddd_registrado != '' and prefixo_A_igual_B == True and (self.ddd_registrado == self.telefoneA[0:2]):
            #  Campo ddd_registrado preenchido e valor digitado é igual ao DDD 
            #  cadastrado da origem, chamada local     
            return f'tctdi:bo=445, anb={Telefone_validoA}, bnb={rn_valido} {self.rop} {Telefone_validoB[2:]}, ea={Telefone_validoA[0:2]}, cl=1, tmr=0;'

        if self.ddd_registrado != '' and prefixo_A_igual_B == True and (self.ddd_registrado != self.telefoneA[0:2]):
            #  Campo ddd_registrado preenchido e o numero digitado é diferente 
            #  do DDD cadastrado, chamada é LD                                   
            return f'tctdi:bo=445, anb={Telefone_validoA}, bnb={rn_valido} {self.rop} 041{self.ddd_registrado}{Telefone_validoB[2:]}, ea={self.ddd_registrado}, cl=1, tmr=0;'


if __name__ =='__main__':
    FormatoTctdi(telefoneA='1185235500', telefoneB='11985235500',ddd_registrado='' , rn='AA123', rop='00000')
    
    
    