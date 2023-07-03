from blueprints.classes.telefone_fixo import telefoneFixo
from blueprints.classes.validacao import validacao
from blueprints.classes.telefone_movel  import telefoneMovel
from blueprints.classes.volte import volte


class tctdiFactory:
        
    @staticmethod
    def criaFormatoTctdi(telefoneA='', telefoneB='', ddd_registrado='', bo='',
                 rn='', rop='', tipo_chamada =''):
        
        validando = validacao(telefoneA, telefoneB, ddd_registrado,
                                      bo, rn, rop)       

        if tipo_chamada == "volte" and validando.validacaoVolte() == True:            
            return volte(telefoneA, telefoneB, ddd_registrado,
                                      bo, rn, rop)
        
        if validando.validacaoTelefoneMovel():
            return telefoneMovel(telefoneA, telefoneB, ddd_registrado,
                                      bo, tipo_chamada = tipo_chamada)
            
        
        if validando.validacaoTelefoneFixo():            
            return telefoneFixo(telefoneA, telefoneB, ddd_registrado,
                                      bo, rn, rop)
        
        return 'Verifique as informações digitadas'
            
        

