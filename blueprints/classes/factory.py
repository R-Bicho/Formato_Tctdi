from blueprints.classes.telefone_fixo import telefoneFixo
from blueprints.classes.validacao import validacao
from blueprints.classes.telefone_movel  import telefoneMovel


class tctdiFactory:
        
    @staticmethod
    def criaFormatoTctdi(telefoneA='', telefoneB='', ddd_registrado='', bo='',
                 rn='', rop=''):
        
        validando = validacao(telefoneA, telefoneB, ddd_registrado,
                                      bo, rn, rop)
        
       
        if validando.validacaoTelefone() == True and len(validando.TelefoneSemCaracterEspecial()[0]) == 11 and validando.validacaoDDD() == True:
            return telefoneMovel(telefoneA, telefoneB, ddd_registrado,
                                      bo)
            
        
        if validando.validacaoTelefone() == True and len(validando.TelefoneSemCaracterEspecial()[0]) == 10 and validando.validacaoDDD() == True and validando.validacaoRN() == True and validando.validacaoROP() == True:            
            return telefoneFixo(telefoneA, telefoneB, ddd_registrado,
                                      bo, rn, rop)
            

