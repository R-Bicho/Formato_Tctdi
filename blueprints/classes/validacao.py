import re

class validacao:

    def __init__(self, telefoneA='', telefoneB='', ddd_registrado='', bo='',
                 rn='', rop=''):
        self.telefoneA = telefoneA
        self.telefoneB = telefoneB
        self.ddd_registrado = ddd_registrado
        self.bo = bo
        self.rn = rn
        self.rop = rop         
        
    def validacaoTelefone(self) -> bool:        

        telefone_regexp = re.compile(r'^([0-9]{2}) ?([0-9]{4,5})-?([0-9]{4})$')
        telefone_0800 = re.compile(r'^(0800) ?([0-9]{3}) ?([0-9]{4})$')

        if telefone_regexp.search(self.telefoneA) and telefone_regexp.search(self.telefoneB):
            return True
        
        elif telefone_regexp.search(self.telefoneA) and telefone_0800.search(self.telefoneB):
            return True
        
        return False
        

    def validacaoDDD(self) -> bool:
        ddd_regexp = re.compile(r'^[0-9]{2}$')

        if ddd_regexp.search(self.ddd_registrado) or self.ddd_registrado == '':
            return True
        return False  
       

    def validacaoRN(self) -> bool:
        rn_regexp = re.compile(r'^[Aa]{1,2}[0-9]{3,4}$')

        if rn_regexp.search(self.rn) and len(self.rn) == 5:
            return True
        return False


    def validacaoROP(self) -> bool:
        rop_regexp = re.compile(r'^[0-9]{5}$')

        if rop_regexp.search(self.rop):
            return True
        return False

    def TelefoneSemCaracterEspecial(self) -> tuple:
        Telefone_validoA = ''
        Telefone_validoB = ''

        for valor in self.telefoneA:
            if valor != ' ' and valor != '-':
                Telefone_validoA += valor

        for valor in self.telefoneB:
            if valor != ' ' and valor != '-':
                Telefone_validoB += valor

        
        return Telefone_validoA, Telefone_validoB   


